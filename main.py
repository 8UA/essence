from googlesearch import search
from linecache import getline
import urllib.request as ul
from bs4 import BeautifulSoup as soup
from loader import Loader
from time import sleep
import sys

##################
# CONFIGURATIONS #
#   \/\/\/\/     #
##################
numpages = 10  # can show less results for certain queries
enctype = 'utf-8'


print("""
    ┌─┐┌─┐┌─┐┌─┐┌┐┌┌─┐┌─┐
─── ├┤ └─┐└─┐├┤ ││││  ├┤  ───
    └─┘└─┘└─┘└─┘┘└┘└─┘└─┘
""")


"""
Requiring user input to make a Google search
and show a little loading animation while looking for results.
"""

while True:
    query = input('Search -> ')
    
    if query == '':
        sys.stdout.write("\x1b[1A\x1b[2K") # deletes last printed string
        continue
    else:
        break

load = Loader("Searching...", "Search Complete.\n", 0.10).start()

"""
Using the googlesearch module to search for results,
write a file listing all the urls and stop the loading animation.
"""

results = open('results.temp', 'w', encoding=enctype)

for url in search(query, tld="co.in", num=numpages, stop=numpages):
    results.write(f'{url}\n')

results.close()

load.stop()

"""
Printing each individual url from file
with corresponding numbers.
"""

# Links with corresponding numbers
page_num = 0
with open('results.temp', 'r') as f:
    for line in f:
        page_num += 1
        print(f'{page_num} | {line.rstrip()}\n')

# Number of links found
with open('results.temp', 'r') as f:
    for count, line in enumerate(f):
        pass
    print('Total Links: ', count + 1)


"""
Getting the number of the page from user input 
and showing the selected url.
"""

while True:
    try:
        page_opt = int(input('Page number > '))
    except ValueError:
        sys.stdout.write("\x1b[1A\x1b[2K")
        print("Please input the number of a page.")
        sleep(1.5)
        sys.stdout.write("\x1b[1A\x1b[2K")
        continue
    else:
        break

page_opt_url = getline('results.temp', page_opt)
print(f"\n{page_opt_url}")


"""
Sending a request to the selected url, parse the html page
to scrape the web page text and write the scraped text into a file.
"""

req = ul.Request(page_opt_url)
html_page = ul.urlopen(req)

soup = soup(html_page, "html.parser")
html_text = soup.get_text()

f = open("html_text.txt", "w", encoding=enctype)  # Creating html_text.txt File
for line in html_text:
    f.write(line)
f.close()


"""
Print final result and exit program.
"""

with open("html_text.txt", "r", encoding=enctype) as f:
    lines = f.read()
    print(lines)

sys.exit()
