# RepoCleaner

This CLEAN.py program will delete all the files listed in your .gitignore file.
It will NOT delete itself, so you can add "CLEAN.py" to your .gitignore file without any fear.\
To clean your folder, you just have to execute it:\
`python3 CLEAN.py`


## Customization

This program has the following functions:

* `read_file()` reads the .gitignore file by default. You can change this file by changing the name inside the function. Here you can also modify which files and folders should be ignored.

* `clean_directory()` will only remove the files, BUT NOT the empty directories.

* `clean_directory_r()` will remove the files AND the empty directories.

By default only files are deleted, BUT NOT empty directories; if you want to remove them too, you need to change the comment in the last lines of code, so comment `clean_directory()` and uncomment `clean_directory_r()`, or vice-versa if you only want files but not empty folders to be removed.