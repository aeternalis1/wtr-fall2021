import numpy as np
import matplotlib.pyplot as plt
from sklearn import metrics

def plot_roc(model_type):

	good_in = open("output/%s_good.txt" % model_type, "r")
	bad_in = open("output/%s_bad.txt" % model_type, "r")

	good_lines = good_in.readlines()
	bad_lines = bad_in.readlines()

	y = np.array([0 for x in range(len(good_lines))] + [1 for x in range(len(bad_lines))])
	scores = np.array([float(x) for x in good_lines] + [float(x) for x in bad_lines])

	fpr, tpr, thresholds = metrics.roc_curve(y, scores)

	np.set_printoptions(threshold=np.inf)

	roc_auc = metrics.auc(fpr, tpr)

	plt.figure()
	lw = 2
	plt.plot(
	    fpr,
	    tpr,
	    color="darkorange",
	    lw=lw,
	    label="ROC curve (area = %0.2f)" % roc_auc,
	)
	plt.plot([0, 1], [0, 1], color="navy", lw=lw, linestyle="--")
	plt.xlim([0.0, 1.0])
	plt.ylim([0.0, 1.05])
	plt.xlabel("False Positive Rate")
	plt.ylabel("True Positive Rate")
	plt.title("Receiver operating characteristic example")
	plt.legend(loc="lower right")
	plt.show()


if __name__ == "__main__":
	plot_roc("bigram")