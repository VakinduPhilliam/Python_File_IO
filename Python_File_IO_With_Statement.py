# Python File IO
# Some standard Python objects now support the context management protocol and can be used with
# the ‘with’ statement.
# After this statement has executed, the file object in f will have been automatically closed, even 
# if the for loop raised an exception part-way through the block.
# Note:
# In this case, f is the same object created by open(), because file.__enter__() returns self.
 
with open('/etc/passwd', 'r') as f:

    for line in f:
        print line

#        ... more processing code ...
