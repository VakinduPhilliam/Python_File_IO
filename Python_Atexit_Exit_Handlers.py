# Python atexit — Exit handlers
# The atexit module defines functions to register and unregister cleanup functions.
# Functions thus registered are automatically executed upon normal interpreter termination.
# atexit runs these functions in the reverse order in which they were registered; if you register A, B, and C, at interpreter termination
# time they will be run in the order C, B, A.
#
# The following simple example demonstrates how a module can initialize a counter from a file when it is imported and save the counter’s
# updated value automatically when the program terminates without relying on the application making an explicit call into this module at
# termination.
 
try:
    with open("counterfile") as infile:
        _count = int(infile.read())

except FileNotFoundError:
    _count = 0

def incrcounter(n):

    global _count
    _count = _count + n

def savecounter():
    with open("counterfile", "w") as outfile:

        outfile.write("%d" % _count)

import atexit

atexit.register(savecounter)
