#!/usr/bin/env python

import sys
import subprocess
# Reference: http://stackoverflow.com/questions/4499910/how-to-display-a-specific-users-commits-in-svn-log#answers
import xml.etree.ElementTree as ET
# Reference: http://docs.python.org/library/optparse.html
from optparse import OptionParser
import pprint

parser = OptionParser();
parser.add_option("-a", "--author", dest="author", help="Author who commit to svn")
parser.add_option("-r", "--revision", dest="revision", help="Start from which revision")

(options, args) = parser.parse_args()

def getXml():
    p = subprocess.Popen(['svn', 'log', '--xml', '-v', '-r', options.revision], stdout=subprocess.PIPE)
    out, err = p.communicate()
    return out

xml = getXml()

for logentry in ET.fromstring(xml):
    if logentry.find('author').text == options.author:
        ET.dump(logentry)

print options.author+"\n"
print options.revision
