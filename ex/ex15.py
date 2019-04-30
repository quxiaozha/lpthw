# -- coding: utf-8 --

print "Type the file name:",
file_name = raw_input(">")

txt = open(file_name)

print txt.read()

txt.close()
