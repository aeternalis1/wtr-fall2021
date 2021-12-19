infile = open("english_dictionary.txt", "r", encoding="utf-8")
outfile = open("clean_english_dictionary.txt", "w")

words = []

for word in infile.read().lower().split():
	clean_word = "".join([x for x in word if 'a' <= x <= 'z'])
	if clean_word:
		words.append(clean_word)

for word in words:
	outfile.write("$" + word + "$\n")
