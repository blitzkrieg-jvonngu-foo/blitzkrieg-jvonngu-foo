###########################################################################################
## Author: nhatNguyen (blitzkrieg-j)                                                     ##
## Python-version: 3.11                                                                  ##
## Source: https://www.github.com/blitzkrieg-jvonngu-foo/blitzkrieg-jvonngu-foo          ##
## Profile-link: https://www.github.con/blitzkrieg-jvonngu-foo                           ##
###########################################################################################

import random as rd

GREAT_LIST_PATH = './src/great_list.txt'  # The list of quotes's index which will be loaded
SOURCE_PATH = './src/sources.txt'
README_PATH = './README.md'

quotes = []

with open(SOURCE_PATH, 'r') as f:
    lines = f.readlines()

# Make source file to kind of lists (author1, quote1), (author2, quote2), ...
# This support for format: '<Name of author>: "<Quote>"'
for line in lines:
    try:
        _index = line.index(':')
    except ValueError:
        continue
    author = line[:_index].strip()
    quote = line[(_index + 1):].strip()
    quotes.append((author, quote))

# Check if great_list file exists, if not, creating new file instead.
try:
    with open(GREAT_LIST_PATH, 'x') as f:
        pass
except FileExistsError:
    pass

# This support for updating new quote not coincide.
# The list of great_list will be got from great_list.txt.
# Choose an index from it and load a specify quote by index and remove the
# index out of great_list.
# Override great_list.txt by great_list's values, the next time run will not
# load the current quote.
# If great_list.txt is empty because of loading all quotes, the quote updating
# will be reset to be as the first time (full of all quotes).
with open(GREAT_LIST_PATH, 'r+') as f:
    f_content = f.read().split()
    great_list = list(range(0, len(quotes)))
    try:
        if len(f_content) > 0:
            great_list = [int(i.strip()) for i in f_content]
        today_random_quote_to_show = rd.choice(great_list)
        great_list.remove(today_random_quote_to_show)
    except ValueError:
        today_random_quote_to_show = rd.randint(0, len(quotes) - 1)
    f.seek(0)
    f.truncate(0)
    f.write(' '.join(str(i) for i in great_list))
    f.flush()

# Handly the align (the client commit doesn't seemly support html format in README.md)
the_quote = ('*' + quotes[today_random_quote_to_show][1] + '*').center(117)
the_author = ('*--' + quotes[today_random_quote_to_show][0] + '--*').center(117)
md_file_content = the_quote.replace(' ', '&nbsp;')\
                + '\n\n' + the_author.replace(' ', '&nbsp;')

# Update README.md
with open(README_PATH, 'w') as f:
    f.write(md_file_content)
    f.flush()

# Thank if you read it and sorry because my non-native English.
