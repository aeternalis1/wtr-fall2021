from random import shuffle

infile = open("clean_corpus.txt", "r")
test_data = open("test_set.txt", "w")
train_data = open("train_set.txt", "w")

words = infile.read().split()

shuffle(words)

ind = len(words) // 5

test_data.write("\n".join(words[:ind]))
train_data.write("\n".join(words[ind:]))