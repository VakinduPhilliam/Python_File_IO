# Python File IO.
# Reading from and Writing to a File.

# Write to a file.

out_file = open("test.txt", "w")
out_file.write("This Text is going to out file\nLook at it and see!")
out_file.close()

# Read from a file

in_file = open("test.txt", "r")
text = in_file.read()
in_file.close()

#
# OUTPUT:
#
# The output and the contents of the file test.txt are:
# This Text is going to out file
# Look at it and see!

#
# REMEMBER:
#
# 'r' - open for reading (default).
# 'w' - open for writing, truncating the file first.
# 'x' - open for exclusive creation, failing if the file already exists.
# 'a' - open for writing, appending to the end of the file if it exists.
# 'b' - binary mode.
# 't' - text mode (default).
# '+' - open a disk file for updating (reading and writing).
# 'U' - universal newlines mode (deprecated).
# The default mode is 'r' (open for reading text, synonym of 'rt'). 
# For binary read-write access, the mode 'w+b' opens and truncates the file to 0 bytes. 
# 'r+b' opens the file without truncation.
