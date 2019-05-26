# Python File IO
# pty — Pseudo-terminal utilities.
# The pty module defines operations for handling the pseudo-terminal concept: starting another process and being able
# to write to and read from its controlling terminal programmatically.
# pty.fork() 
# Fork. Connect the child’s controlling terminal to a pseudo-terminal.
# Return value is (pid, fd). Note that the child gets pid 0, and the fd is invalid.
# The parent’s return value is the pid of the child, and fd is a file descriptor connected to the child’s controlling
# terminal (and also to the child’s standard input and output).
#
# The following program acts like the Unix command script(1), using a pseudo-terminal to record all input and output of
# a terminal session in a “typescript”.
# 

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
