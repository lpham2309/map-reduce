#!/usr/bin/env python3

import sys, re
import re
import os
import json
from urllib.parse import unquote_plus

def main(argv):
    # filepath = os.environ["map_input_file"]
    # filename = os.path.split(filepath)[-1]
    views_by_date = {}

    # file_date = int(filename.split("-")[1])
    for line in sys.stdin:
        column_name = line.strip().split("\t")
        wiki_title_accessed_year = column_name[0].split("}")
        print(wiki_title_accessed_year)
        wiki_title = str(wiki_title_accessed_year[0])
        accessed_date = str(wiki_title_accessed_year[1])

        if str(wiki_title) in views_by_date:
            views_by_date[str(wiki_title)] = int(column_name[1])
    
    for key, value in views_by_date.items():
        views_data = {}
        if str(accessed_date) not in views_data and value > 10:
            views_data.update(
                {
                    str(accessed_date): value
                }
            )
            print(key + "\t" + json.dumps(views_data))

    #     filter_special_characters = re.compile(r'[%*%]', flags=re.I | re.X)
    #     filter_html_tags = re.compile(r'<.*?>', flags=re.I | re.X)
    #     if not filter_special_characters.findall(column_name[0]) and column_name[0] == 'en' and len(column_name[1]) > 0 and column_name[1][0].isupper() and not filter_html_tags.findall(column_name[0]):
    #         filter_titles = re.compile(r'Media | Special | Talk | User | User_talk | Project | Project_talk | File | File_talk | MediaWiki | MediaWiki_talk | Template | Template_talk | Help | Help_talk | Category | Category_talk | Portal | Wikipedia | Wikipedia_talk', flags=re.I | re.X)
    #         filter_extension = re.compile(r'\b.jpg | \b.gif | \b.png | \b.JPG | \b.GIF | \b.PNG | \b.ico | \b.txt', flags=re.I | re.X)
    #         filter_boilerplate = re.compile(r'404_error | Main_Page| Hypertext_Transfer_Protocol | Favicon.ico | Search', flags=re.I | re.X)
    #         if not filter_titles.findall(column_name[1]) and not filter_extension.findall(column_name[1]) and not filter_boilerplate.findall(column_name[1]):
    #             curr_title = unquote_plus(column_name[1])
    #             if str(curr_title) in views_by_date:
    #                 views_by_date[str(curr_title)] += int(column_name[2])
    #             else:
    #                 views_by_date[str(curr_title)] = int(column_name[2])
if __name__=="__main__":
    main(sys.argv)