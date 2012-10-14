# SVN Export
Basically this is to copy out those files that have been committed to a external folder.  
It will take from **svn log** to find out all the files from author that you specify and from revision range that you specify.

## Example
```shell
python svnexport.py -r 30:35 -a jslim89 -d ~/export_dir -b branch/foo
```
This example is to show that it will take from:
* revision **30** to **35**
* the author is **jslim89**
* export to **~/export_dir** directory
* the project is from branch named *foo*

This is the sample output
```
Copied: path/to/source1.py -> /home/jslim89/path/to/source1.py
Copied: path/to/source2.py -> /home/jslim89/path/to/source2.py
Copied: path/to/source3.py -> /home/jslim89/path/to/source3.py
```
**Assumed that the home directory is _/home/jslim89/_**

## Options
* -r or --revision    -> Which revision you want to export (Required)
* -a or --author      -> The author who commit the source code (Required)
* -d or --destination -> The destination where you want to copy to (Required)
* -b or --branch      -> The project is from which branch **(NOTE: default is _trunk_)**

## Source Code & Download
* Browse and checkout the [source code](https://github.com/jslim89/svn-export).
* [Download](https://github.com/jslim89/svn-export/archives/master) the project.

## License
Released under the [GPL] (http://www.gnu.org/licenses/gpl.html)
