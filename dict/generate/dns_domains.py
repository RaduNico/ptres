import sys
import os

from itertools import product
from string import ascii_lowercase, digits

if len(sys.argv) != 3:
	print("Usage %s <output_file> <number of digits>")
	sys.exit(-1)

num_digits = int(sys.argv[2])

if num_digits < 1 or num_digits > 5:
	print("Invalid number of digits %s" % sys.argv[2])
	sys.exit(-1)

if os.path.isfile(sys.argv[1]):
	print("File '%s' already exists!" % sys.argv[1])
	sys.exit(-1)

keywords = [''.join(i) for i in product(ascii_lowercase, repeat = num_digits)]


with open(sys.argv[1], "w") as fd:
	for keyword in keywords:
		fd.write("%s\n" % keyword)
