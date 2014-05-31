#! /usr/bin/env python

"""
Input:

139_108	64	FEMALE	167.9	172.1	4.2	104.992	170.072	363.497	169.112	228.206	227.95	46.78644.588	33.623	71.649	168.66	88.654	170.128	83.256	83.442	Yeah, um, I'm originally from San Jose.  So it's like a half an hour drive home.
"""


import json, sys
import fileinput
import string

exclude = set(string.punctuation)

# For each input row
for row in fileinput.input():
  parts = row.strip().split('\t')

  dateid = parts[0]
  text = parts[-1]

  for word in text.lower().split():
	word = ''.join(ch for ch in word if ch not in exclude)

  	print "%s\t%s" % (dateid, word)