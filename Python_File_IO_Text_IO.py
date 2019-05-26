# Python 'io'.
# Core tools for working with streams.
# The io module provides Python’s main facilities for dealing with various types of I/O.
# There are three main types of I/O: text I/O, binary I/O and raw I/O. 
# Text I/O
# Text I/O expects and produces str objects.
# This means that whenever the backing store is natively made of bytes (such as in the case of a file), 
# encoding and decoding of data is made transparently as well as optional translation of platform-specific
# newline characters.
# The easiest way to create a text stream is with open(), optionally specifying an encoding:
 
f = open("myfile.txt", "r", encoding="utf-8")
 
# In-memory text streams are also available as StringIO objects:
 
f = io.StringIO("some initial text data")
