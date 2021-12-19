from random import randint
from utils import lex

outfile = open("data/test_set_bad.txt", "w")

for i in range(400000):
	l = randint(1, 10)
	s = "$" + "".join([lex[randint(0, len(lex)-2)] for x in range(l)]) + "$"
	outfile.write(s + "\n")