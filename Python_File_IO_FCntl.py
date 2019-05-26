# Python File IO
# fcntl — The fcntl and ioctl system calls.
# This module performs file control and I/O control on file descriptors. It is an interface to the fcntl() and ioctl() Unix routines.
# All functions in this module take a file descriptor fd as their first argument.
# This can be an integer file descriptor, such as returned by sys.stdin.fileno(), or an io.IOBase object, such as sys.stdin itself, which
# provides a fileno() that returns a genuine file descriptor.
#
# Examples on a SVR4 compliant system:
# 

import struct, fcntl, os

f = open(...)
rv = fcntl.fcntl(f, fcntl.F_SETFL, os.O_NDELAY)

lockdata = struct.pack('hhllhh', fcntl.F_WRLCK, 0, 0, 0, 0, 0)

rv = fcntl.fcntl(f, fcntl.F_SETLKW, lockdata)
