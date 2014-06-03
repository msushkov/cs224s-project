
import sys

f = sys.argv[1]

lines = open(f).readlines()

tp = float(lines[0].strip())
fp = float(lines[1].strip())
tn = float(lines[2].strip())
fn = float(lines[3].strip())

print "PRECISION: %f" % (tp / (tp + fp))
print "RECALL: %f" % (tp / (tp + fn))
print "F1: %f" % (2.0 * tp / (2.0 * tp + fn + fp))
print "ACCURACY: %f" % ((tp + tn) / (tp + tn + fp + fn))