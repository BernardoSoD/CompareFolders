# CompareFolders
Two simple Python programs to show files inside a directory tree and compare them

### To run it:

# Scan 
(Your Python version must be >=3.5)

Simply go to it's directory in terminal and type:
```
python Scanner.py "%ABSOLUTE_PATH_TO_THE_DESIRED_DIRECTORY%"
```
Example:
`` python Scanner.py "C:\Program Files\Git" `` \
It will generate a .txt file called "output.txt" where each line is a relative path of the file (to the path you chose) and the size of the file in Bytes.

Known issues:

- In some folders it will throw PermissionError,
- It doesn't have exception handling, so Stack Traces may be showing up

# Compare

Simply go to it's directory in terminal and type:
```
python Compare.py "%ABSOLUTE_PATH_FIRST_FILE" "%ABSOLUTE_PATH_SECOND_FILE"
```
Note that the first file must be a version before the second file, in other words, the first file is the older one.

Example:
`` python Compare.py "C:\Program Files\Git" "C:\Program Files\Gitv2" `` \
It will generate a .txt file called "compared.txt" where each line is a relative path of the files (to the path you chose) that are different from the first file or have a different size of a equal file.
