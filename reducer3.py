#!/usr/bin/env python
from operator import itemgetter
import sys

current_key = None
current_list = []
key = None

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    key, location = line.split('\t')
    if current_key == key:
        current_list = current_list + location
    else:
        if current_key:
            # write result to STDOUT
            print '%s\t%s' % (current_key, current_list)
        current_list = location
        current_key = key


if current_key == key:
    print '%s\t%s' % (current_key, current_list)
