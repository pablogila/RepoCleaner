""""

This program cleans the current directory of all the files named in the .gitignore file, excepting for this file itself.
The .gitignore file should be in the same directory as the CLEAN.py file.
This file could have a different name, just make sure to change the name in the read_file() function.
If you also want to remove the empty directories, change the comment in the last lines of the code.

clean_directory() will only remove the files, but not the empty directories.
clean_directory_r() will remove the files AND the empty directories.

"""


import os
import fnmatch


def read_file():
	"""
	Reads the .gitignore file in the current directory and returns a list of file patterns to ignore.
	"""
	patterns = []
	# Now we open the file with the list of files to remove, in this case a .gitignore file
	with open(".gitignore", "r") as f:
		for line in f:
			# Ignore empty lines and comments, as well as this CLEAN.py file
			if line.strip() == "" or line.startswith("#") or line.strip() == "CLEAN.py":
				continue
			patterns.append(line.strip())
	return patterns

def clean_directory():
	"""
	Deletes all files in the current directory that match the patterns in the .gitignore file, but NOT the empty directories.
	"""
	patterns = read_file()
	for root, dirs, files in os.walk("."):
		for name in files:
			path = os.path.join(root, name)
			if any(fnmatch.fnmatch(path, pattern) for pattern in patterns):
				os.remove(path)
				print(f"Deleted {path}")


def clean_directory_r():
	"""
	Deletes all files in the current directory that match the patterns in the .gitignore file, as well as any empty directories.
	"""
	patterns = read_file()
	for root, dirs, files in os.walk("."):
		for name in files:
			path = os.path.join(root, name)
			if any(fnmatch.fnmatch(path, pattern) for pattern in patterns):
				os.remove(path)
				print(f"Deleted {path}")
		for name in dirs:
			path = os.path.join(root, name)
			try:
				os.rmdir(path)
				print(f"Deleted {path}")
			except OSError:
				pass


if __name__ == "__main__":
	clean_directory()
#	clean_directory_r()

