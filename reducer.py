#!/usr/bin/env python3

import sys
import re

def main(argv):
    wiki_count = {}
    for line in sys.stdin:
        wiki_title_data = line.split(" ")
        if len(wiki_title_data) == 3:
            title = wiki_title_data[0]
            count = int(wiki_title_data[1])
            date_accessed = wiki_title_data[2]
            if title not in wiki_count:
                wiki_count[title+"}"+date_accessed] = count
    
    for key, value in wiki_count.items():
        print(key + "\t" + str(value) + "\n")

if __name__=="__main__":
    main(sys.argv)