#!/usr/bin/env python3

import sys
import json

def main(argv):
    wiki_count = {}
    for line in sys.stdin:
        try:
            wiki_title_data = line.split("\t")
            if wiki_title_data and len(wiki_title_data) == 2:
                title = wiki_title_data[0]
                if wiki_title_data[1] is not None and '{' in wiki_title_data[1]:
                    try:
                        views_date_data = json.loads(wiki_title_data[1])
                    except Exception as e:
                        print('Error parsing values: {} with inputs {}'.format(e, wiki_title_data))
                    if title not in wiki_count:
                        wiki_count[title] = views_date_data
        except EOFError as e:
            print('Error: ', e)

    for key, val in wiki_count.items():
        accessed_date = list(val.keys())
        views_count = list(val.values())
        totalSum = sum(views_count)
        popularity_trend = sum(views_count[2:]) - sum(views_count[:2])

        print(key + "\t" + str(accessed_date) + "\t" + str(views_count) + "\t" + str(totalSum) + "\t" + str(popularity_trend))
if __name__=="__main__":
    main(sys.argv)