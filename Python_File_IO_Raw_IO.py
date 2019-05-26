# Python 'io'.
# Core tools for working with streams.
# The io module provides Python’s main facilities for dealing with various types of I/O.
# There are three main types of I/O: text I/O, binary I/O and raw I/O. 
# Raw I/O.
# Raw I/O (also called unbuffered I/O) is generally used as a low-level building-block for binary
# and text streams; it is rarely useful to directly manipulate a raw stream from user code.
# Nevertheless, you can create a raw stream by opening a file in binary mode with buffering disabled:
 
f = open("myfile.jpg", "rb", buffering=0)
