Remove Whitespace
==============
 Reformats .txt files that start with EASI, removes unnecessary lines that start with whitespace, and preserves necessary lines while removing trailing whitespace
 
 Usage
 --------------
1. [Requires Python3](https://realpython.com/installing-python/)
2. You can place formatData.py in the folder containing the files you want to format, and when run from command line as below(without arguments):
```
$ python3 formatData.py
No directory provided, formatting current directory
Formatting files in /Users/currentfolder
```
 the script will go through every .txt file in the folder and remove excess data/errors/whitespace

3. You can also provide an argument in the command line to target a different directory as below:
```
$ python3 formatData.py /Users/[whateverfolderyouwant]/
Formatting files in Folder:/Users/whateverfolderyouwant/
```
the script will perform the same function in that folder instead.

Tested on Mac, may need modification to run correctly on windows