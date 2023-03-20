#!/usr/bin/env python3

import sys, re
import re
import os
from urllib.parse import unquote_plus

def main(argv):
    article_info = {}
    filepath = os.environ["map_input_file"]
    filename = os.path.split(filepath)[-1]
    
    file_date = filename.split("-")[1]
    for line in sys.stdin:
        row = line.split(" ")
        filter_special_characters = re.compile(r'[%*%]', flags=re.I | re.X)
        if not filter_special_characters.findall(row[0]) and row[0] == 'en' and len(row[1]) > 0 and row[1][0].isupper() and "<a" not in row[0]:
            filter_titles = re.compile(r'Media | Special | Talk | User | User_talk | Project | Project_talk | File | File_talk | MediaWiki | MediaWiki_talk | Template | Template_talk | Help | Help_talk | Category | Category_talk | Portal | Wikipedia | Wikipedia_talk', flags=re.I | re.X)
            filter_extension = re.compile(r'\b.jpg | \b.gif | \b.png | \b.JPG | \b.GIF | \b.PNG | \b.ico | \b.txt', flags=re.I | re.X)
            filter_boilerplate = re.compile(r'404_error | Main_Page| Hypertext_Transfer_Protocol | Favicon.ico | Search', flags=re.I | re.X)
            if not filter_titles.findall(row[1]) and not filter_extension.findall(row[1]) and not filter_boilerplate.findall(row[1]):
                curr_title = unquote_plus(row[1])
                if str(curr_title) in article_info:
                    article_info[str(curr_title)] += int(row[2])
                else:
                    article_info[str(curr_title)] = int(row[2])

    for key, value in article_info.items():
        print(key + " " + str(value) + " " + file_date)
if __name__=="__main__":
    main(sys.argv)