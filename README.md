# SVN Export
Basically this is to copy out those files that have been committed to a external folder.  
It will take from **svn log** to find out all the files from author that you specify and from revision range that you specify.

## Usage
**NOTE: Please ensure that your svnexport.py is place inside the project _root dir_**
```shell
python svnexport.py -r 30:35 -a jslim89 -d ~/export_dir -b branch/foo -f filename.txt -p file_path_prefix/path/to/file
```
This example is to show that it will take from:
* revision **30** to **35**
* the author is **jslim89**
* export to **~/export_dir** directory
* the project is from branch named *foo*
* it will output to a file named filename.txt in current path which contain the file path of the exported file
* can add a prefix in front of the file path

This is the sample output
```
Copied: path/to/source1.py -> /home/jslim89/export_dir/path/to/source1.py
Copied: path/to/source2.py -> /home/jslim89/export_dir/path/to/source2.py
Copied: path/to/source3.py -> /home/jslim89/export_dir/path/to/source3.py
```
**Assumed that the home directory is _/home/jslim89/_**

## Options
* -r or --revision    -> Which revision you want to export (Required)
* -a or --author      -> The author who commit the source code (Required)
* -d or --destination -> The destination where you want to copy to (Required)
* -b or --branch      -> The project is from which branch **(NOTE: default is _trunk_)**
* -f or --filename    -> The filename for the output file which contain the exported file path (optional)
* -p or --file_prefix -> The prefix for the file path for the output file (optional)

## Source Code & Download
* Browse and checkout the [source code](https://github.com/jslim89/svn-export).
* [Download](https://github.com/jslim89/svn-export/archives/master) the project.
