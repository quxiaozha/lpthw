# -- coding: utf-8 --

target = open("ex15_sample.txt", 'w')

# print target.read()

print "Truncating the file , Bye~"

target.truncate()

# print target.read()

print 'oh, fuck ! the file is empty'
print "Now pls input something, i will write to the file~"

line1 = raw_input('line1:')
line2 = raw_input('line2:')
line3 = raw_input('line3:')

target.write(line1)
target.write('\n')

target.write(line2)
target.write('\n')

target.write(line3)
target.write('\n')

print "done! let me have a look~"

# print target.read()

print "yes! we got it!"
