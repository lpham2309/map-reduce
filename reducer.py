#!/usr/bin/env python3

import sys
import re

def main(argv):
    wiki_count = {}
    for line in sys.stdin:
        wiki_title_data = line.split(" ")
        if len(wiki_title_data) == 3:
            title = wiki_title_data[0]
            count = wiki_title_data[1]
            date_accessed = wiki_title_data[2]
            trimmed_date = date_accessed.replace("\n", "")
            if title not in wiki_count:
                title_with_accessed_date = title+ "}" + trimmed_date
                wiki_count[title_with_accessed_date] = count
    for key, value in wiki_count.items():
        print(key+"\t"+str(value))

if __name__=="__main__":
    main(sys.argv)