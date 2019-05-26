# Python 'io'.
# Core tools for working with streams.
# The io module provides Python’s main facilities for dealing with various types of I/O.
# There are three main types of I/O: text I/O, binary I/O and raw I/O. 
# I/O Base Classes.
# class 'io.IOBase' is the abstract base class for all I/O classes, acting on streams of bytes.
# There is no public constructor.
# IOBase is also a context manager and therefore supports the with statement.
# In this example, file is closed after the 'with' statement’s suite is finished—even if an
# exception occurs:
 
with open('spam.txt', 'w') as file:

    file.write('Spam and eggs!')
