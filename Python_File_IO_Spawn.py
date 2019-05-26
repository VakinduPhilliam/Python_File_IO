# Python File IO
# pty.spawn(argv[, master_read[, stdin_read]]). 
# Spawn a process, and connect its controlling terminal with the current process�s standard io.
# This is often used to baffle programs which insist on reading from the controlling terminal.
# The functions master_read and stdin_read should be functions which read from a file descriptor.
# The defaults try to read 1024 bytes each time they are called.
# spawn() now returns the status value from os.waitpid() on the child process.
# 
# Example:
# 
# The following program acts like the Unix command script(1), using a pseudo-terminal to record all input
# and output of a terminal session in a �typescript�.
 
import argparse
import os
import pty
import sys
import time

parser = argparse.ArgumentParser()
parser.add_argument('-a', dest='append', action='store_true')
parser.add_argument('-p', dest='use_python', action='store_true')
parser.add_argument('filename', nargs='?', default='typescript')

options = parser.parse_args()

shell = sys.executable if options.use_python else os.environ.get('SHELL', 'sh')
filename = options.filename

mode = 'ab' if options.append else 'wb'

with open(filename, mode) as script:

    def read(fd):
        data = os.read(fd, 1024)

        script.write(data)

        return data

    print('Script started, file is', filename)

    script.write(('Script started on %s\n' % time.asctime()).encode())

    pty.spawn(shell, read)

    script.write(('Script done on %s\n' % time.asctime()).encode())

    print('Script done, file is', filename)
