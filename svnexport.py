#!/usr/bin/env python

import sys
import subprocess
import os
import shutil
# Reference: http://stackoverflow.com/questions/4499910/how-to-display-a-specific-users-commits-in-svn-log#answers
import xml.etree.ElementTree as ET
# Reference: http://docs.python.org/library/optparse.html
from optparse import OptionParser

parser = OptionParser();
parser.add_option("-a", "--author", dest="author", help="Author who commit to svn")
parser.add_option("-r", "--revision", dest="revision", help="Start from which revision")
parser.add_option("-d", "--destination", dest="destination", help="Destination where you want to export")
parser.add_option("-b", "--branch", dest="branch", default="trunk", help="Whether the project is in 'trunk' or 'branch'")

(options, args) = parser.parse_args()

def getXml():
    p = subprocess.Popen(['svn', 'log', '--xml', '-v', '-r', options.revision], stdout=subprocess.PIPE)
    out, err = p.communicate()
    return out

def getFileList(xml):
    fileList = []
    for logentry in ET.fromstring(xml).findall('logentry'):
        if logentry.find('author').text != options.author:
            continue
        for path in logentry.find('paths').findall('path'):
            # will not be export if the file is deleted or ignored
            if path.get('action') == 'D' or path.get('action') == 'I':
                continue
            # path.text should output like this "/trunk/path/to/source.py"
            # only replace the first occurance
            filePath = path.text.replace("/"+options.branch+"/", "", 1)
            # will not be added again if the element is existed in the list
            # NOTE: similar to php "in_array($path.text, $fileList)"
            if filePath in fileList:
                continue
            fileList.append(filePath)
    return fileList

# Reference: http://stackoverflow.com/questions/12842997/how-to-copy-a-file-using-python#answers
def cp(src, dst):
    assert not os.path.isabs(src)
    dstdir = os.path.join(dst, os.path.dirname(src))
    if not os.path.exists(dstdir):
        os.makedirs(dstdir)
    dstfile = os.path.join(dst, src)
    shutil.copyfile(src, dstfile)
    print "Copied: "+src+" -> "+dstfile

def main():
    files = getFileList(getXml())
    for f in files:
        cp(f, options.destination)

main()
