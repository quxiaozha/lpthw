# -- coding: utf-8 --

from os.path import exists

from_file = 'from.txt'
to_file = 'to.txt'

print 'Copying from %s to %s' % (from_file, to_file)

indata = open(from_file).read()

print 'The input file is %d bytes long' % len(indata)

print 'Does the output file exist? %r' % exists(to_file)

print 'Ready, hit RETURN to continue, CTRL-C to abort.'

raw_input()

output = open(to_file, 'w')

output.write(indata)

# output.flush()

print 'Alright, all done'

output.close()
