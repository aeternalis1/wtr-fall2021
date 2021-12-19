from utils import get_bigrams, lex

infile = open("data/clean_corpus.txt", "r")
outfile = open("models/bigram_model.txt", "w")

count = [[0 for x in range(len(lex))] for x in range(len(lex))]

for word in infile.read().split():
	for a, b in get_bigrams(word):
		count[lex.find(a)][lex.find(b)] += 1

for i in range(len(lex)):
	row = [count[i][j] / max(sum(count[i]), 1) for j in range(len(lex))]
	outfile.write(" ".join(str(x) for x in row) + "\n")
