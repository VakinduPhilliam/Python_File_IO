# Python 'io'.
# Core tools for working with streams.
# The io module provides Python’s main facilities for dealing with various types of I/O.
# There are three main types of I/O: text I/O, binary I/O and raw I/O. 
# Binary I/O.
# Binary I/O (also called buffered I/O) expects bytes-like objects and produces bytes objects. 
# No encoding, decoding, or newline translation is performed.
# This category of streams can be used for all kinds of non-text data, and also when manual control 
# over the handling of text data is desired.
# The easiest way to create a binary stream is with open() with 'b' in the mode string:
 
f = open("myfile.jpg", "rb")
 
# In-memory binary streams are also available as BytesIO objects:
 
f = io.BytesIO(b"some initial binary data: \x00\x01")
