import numpy as np
from keras.datasets import imdb
from keras.models import Sequential, load_model
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers.embeddings import Embedding
from keras.preprocessing import sequence
from sklearn.metrics import roc_curve
from utils import lex


MAX_WORD_LENGTH = 20


def normalize_words(lines, max_word_length):
	return sequence.pad_sequences([[lex.find(x) for x in line.strip()] for line in lines], maxlen=max_word_length)


def train_model():
	# fix random seed for reproducibility
	np.random.seed(7)

	good_train_file = open("data/train_set.txt", "r")
	good_test_file = open("data/test_set.txt", "r")
	bad_train_file = open("data/train_set_bad.txt", "r")
	bad_test_file = open("data/test_set_bad.txt", "r")

	good_train_lines = good_train_file.readlines()
	bad_train_lines = bad_train_file.readlines()
	X_train_lines = good_train_lines + bad_train_lines
	y_train = np.array([0 for x in range(len(good_train_lines))] + [1 for x in range(len(bad_train_lines))])

	good_test_lines = good_test_file.readlines()
	bad_test_lines = bad_test_file.readlines()
	X_test_lines = good_test_lines + bad_test_lines
	y_test = np.array([0 for x in range(len(good_test_lines))] + [1 for x in range(len(bad_test_lines))])

	# truncate and pad input sequences
	X_train = normalize_words(X_train_lines, MAX_WORD_LENGTH)
	X_test = normalize_words(X_test_lines, MAX_WORD_LENGTH)

	# create the model
	embedding_vector_length = 32
	model = Sequential()
	model.add(Embedding(len(lex), embedding_vector_length, input_length=MAX_WORD_LENGTH))
	model.add(LSTM(100))
	model.add(Dense(1, activation='sigmoid'))
	model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
	print(model.summary())
	model.fit(X_train, y_train, epochs=3, batch_size=64)

	# Final evaluation of the model
	scores = model.evaluate(X_test, y_test, verbose=0)
	print("Accuracy: %.2f%%" % (scores[1]*100))
	model.save('models/lstm_model')


def test_model():
	model = load_model('models/lstm_model')

	good_test_file = open("data/test_set.txt", "r")
	bad_test_file = open("data/test_set_bad.txt", "r")
	good_out = open("output/lstm_good.txt", "w")
	bad_out = open("output/lstm_bad.txt", "w")

	good_lines = good_test_file.readlines()
	bad_lines = bad_test_file.readlines()

	good_test = normalize_words(good_lines, MAX_WORD_LENGTH)
	bad_test = normalize_words(bad_lines, MAX_WORD_LENGTH)

	good_pred_keras = model.predict(good_test).ravel()
	bad_pred_keras = model.predict(bad_test).ravel()

	good_out.write("\n".join(str(x) for x in good_pred_keras))
	bad_out.write("\n".join(str(x) for x in bad_pred_keras))


if __name__ == "__main__":
	test_model()