# -- coding: utf-8 --


def print_two(*args):
    arg1, arg2 = args
    print 'arg1: %r, arg2: %r' % (arg1, arg2)


print_two('first', 22222)
