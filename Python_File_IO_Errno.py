# Python File IO
# Displaying File Load Errors
# The hierarchy of exceptions raised by operating system errors
# OS Errors can now also written without the errno import and without manual
# inspection of exception attributes:

try:
    with open("document.txt") as f:
        content = f.read()

except FileNotFoundError:
    print("document.txt file is missing")

except PermissionError:
    print("You are not allowed to read document.txt")
