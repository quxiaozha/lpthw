# -- coding: utf-8 --

formatter = '%r %r %r %r'

print formatter % (1, 2, 3, 4)
print formatter % ('one', 2, 'three', "four")

print formatter % (formatter, formatter, formatter, formatter)

print formatter % (
    "I have get it",
    "That u",
    "But he did't know",
    "So do u do"
)