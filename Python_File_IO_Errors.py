# Python File IO
# Displaying File Load Errors
# The hierarchy of exceptions raised by operating system errors

from errno import ENOENT, EACCES, EPERM

try:
    with open("document.txt") as f:
        content = f.read()

except IOError as err:

    if err.errno == ENOENT:
        print("document.txt file is missing")

    elif err.errno in (EACCES, EPERM):
        print("You are not allowed to read document.txt")

    else:
        raise
