from utils import get_bigrams, lex

model_file = open("models/bigram_model.txt", "r")
good_in = open("data/clean_english_dictionary.txt", "r")
bad_in = open("data/test_set_bad.txt", "r")
good_out = open("output/bigram_good.txt", "w")
bad_out = open("output/bigram_bad.txt", "w")

good_tests = good_in.read().split()
bad_tests = bad_in.read().split()
model = [list(map(float, line.split())) for line in model_file.readlines()]

def bigram_prob(word):
	bigrams = get_bigrams(word)
	return 1 - sum(model[lex.find(x[0])][lex.find(x[1])] for x in bigrams) / len(bigrams)

good_out.write("\n".join(str(bigram_prob(x)) for x in good_tests))
bad_out.write("\n".join(str(bigram_prob(x)) for x in bad_tests))
