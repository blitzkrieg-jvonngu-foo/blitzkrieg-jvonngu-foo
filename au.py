import random as rd

GREAT_LIST_PATH = './src/great_list.txt'
SOURCE_PATH = './src/sources.txt'
README_PATH = './README.md'
quotes = []
with open(SOURCE_PATH, 'r') as f:
    lines = f.readlines()

for line in lines:
    try:
        _index = line.index(':')
    except ValueError:
        continue
    author = line[:_index].strip()
    quote = line[(_index + 1):].strip()
    quotes.append((author, quote))
try:
    with open(GREAT_LIST_PATH, 'x') as f:
        pass
except FileExistsError:
    pass

with open(GREAT_LIST_PATH, 'r+') as f:
    f_content = f.read().split()
    great_list = list(range(0, 12))
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

the_quote = ('*' + quotes[today_random_quote_to_show][1] + '*').center(117)
the_author = ('*--' + quotes[today_random_quote_to_show][0] + '--*').center(117)
md_file_content = the_quote.replace(' ', '&nbsp;')\
                + '\n\n' + the_author.replace(' ', '&nbsp;')
with open(README_PATH, 'w') as f:
    f.write(md_file_content)
    f.flush()

