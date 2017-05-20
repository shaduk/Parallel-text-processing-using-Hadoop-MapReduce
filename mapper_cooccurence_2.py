#!/usr/bin/env python

import sys
import csv
import re

mydict = {}
reader = csv.reader(open('new_lemmatizer.csv'), delimiter = ',')
i = 0
for row in reader:
	key = row[0]
	if key in mydict:
		pass
	mydict[key] = filter(None, row[1:])
c = 0
# input comes from STDIN (standard input)
for line in sys.stdin:
    line = line.strip()
    if(len(line.split(">")) <= 1):
		continue
    location, words = line.split(">")
    location = location + ">"
    words = words.split()
    for i in range(0, len(words)):
		for j in range(i+1, len(words)):
			word1 = " ".join(re.findall("[a-zA-Z]+", words[i]))
			word1 = word1.replace("j", "i")
			word1 = word1.replace("v", "u")
			word2 = " ".join(re.findall("[a-zA-Z]+", words[j]))
			word2 = word2.replace("j", "i")
			word2 = word2.replace("v", "u")
			if word1 in mydict:
				if mydict[word1] != "":
					word1 = mydict[word1]
			else:
				word1 = [word1]
			if word2 in mydict:
				if mydict[word2] != "":
					word2 = mydict[word2]
			else:
				word2 = [word2]
			pairs = word1 + word2
			print '%s\t%s' % (pairs, location)

