# Python 'io'.
# Core tools for working with streams.
# The io module provides Python’s main facilities for dealing with various types of I/O.
# There are three main types of I/O: text I/O, binary I/O and raw I/O. 
# getvalue(). 
# Return a 'str' containing the entire contents of the buffer.
# Newlines are decoded as if by read(), although the stream position is not changed.
# Example:
 
import io

output = io.StringIO()
output.write('First line.\n')

print('Second line.', file=output)

# Retrieve file contents -- this will be
# 'First line.\nSecond line.\n'

contents = output.getvalue()

# Close object and discard memory buffer --
# .getvalue() will now raise an exception.

output.close()
