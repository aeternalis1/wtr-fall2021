lex = "abcdefghijklmnopqrstuvwxyz$"

def get_bigrams(s):
	bigrams = []
	for i in range(len(s)-1):
		bigrams.append(s[i:i+2])
	return bigrams