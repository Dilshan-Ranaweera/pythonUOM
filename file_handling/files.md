# File Handling
## 1) Opening a file
```markdown
Before performing any file operations on a file, the file needs to be opened. The open() function in python facilitates opening files in Python. Open function opens the required file and provides us with a special pointer called a file handle. A file handle is a special variable that links our python program to the file and helps us perform various file operations.

While opening files, Python allows us to specify a file opening mode, which indicates the purpose of opening the file. For example, we can tell python that we want to open a file only for reading or for both reading and writing.

 

To open a file, you must provide the name of the file that you want to open as a string. In addition to the file name, you can also optionally specify the file opening mode. There are many file opening modes. The simplest opening modes are read ‘r’ and write ‘w’, which opens the file for reading and writing, respectively.  
```
## 2) Reading a file
```
After opening the file, the file content can be read using various python functions. read() function reads the whole file at once whereas the readline() function reads the file line by line. To read a file, the file should be opened in read mode and the opened file should be assigned to a file handle. While opening a file, if a mode is not explicitly specified, Python opens the file in read mode.

While performing file operations that deal with files line by line, such as the readline() function, Python identifies the end of each line by a special character called the newline character. Newline character is written as “\n” and is placed at the end of each line. While printing a sequence of characters, whenever a newline character is encountered, python goes to the next line before printing the next character.

```
## 3) Writing to a file
```
To write to a file, we have to open the file in write mode. To do that, we can spec the mode as “w” while calling the open function. Once opened, we can use the function write() to write a given string to the file.
```
## 4) Closing a file
```
After we are done with the file operations, we should close the file we opened. Python may automatically close any opened file when the file is reassigned to a different file handle. However, it is a good programming practice to close the file after use.
```
## 5) File handling errors
```
Whatever the mode that we try to open the file with, you can encounter a situation in which the file you are trying to open does not exist in the specified file path or the current directory.

In such a situation, depending on the file opening mode, python will take different actions.

If the file open mode is r, or read, python will show an error saying that the file cannot be found.

If the file open mode is w, or write, python will create a new file named with filename specified if it does not already exist.
```

