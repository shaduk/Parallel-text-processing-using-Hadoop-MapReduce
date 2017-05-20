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

# input comes from STDIN (standard input)
for line in sys.stdin:
	line = line.strip()
	if(len(line.split(">")) > 1):
		location, words = line.split(">")
		location = location + ">"
	else:
		continue
	words = words.split()
	for word in words:
		word = " ".join(re.findall("[a-zA-Z]+", word))
		word = word.replace("j", "i")
		word = word.replace("v", "u")
		if word in mydict:
			for lemma in mydict[word]:
				print '%s\t%s' % (lemma, location)
		elif word != '':
			print '%s\t%s' % (word, location)
			
			
			 
