# DirectoryScan
A simple Python program to output files inside a directory tree

### To run it:

(Your Python version must be >=3.5)

Simply go to it's directory and type:
```
python Scanner.py "%ABSOLUTE_PATH_TO_THE_DESIRED_DIRECTORY%"
```
Example:
`` python Scanner.py "C:\Program Files\Git" `` \
It will generate a .txt file called "saida.txt" where each line is a relative path of the file (to the path you chose) and the size of the file in Bytes.

Known issues:

- In some folders it will throw PermissionError,
- It doesn't have exception handling, so Stack Traces may be showing up

#### Why I made it

My internet connection speed is trash and me and my brother will have to download the new Season CoD Update, so I'm doing this so I can see which files are new or overwritten, so instead of downloading the update two times, he can pass to me only what changed.
