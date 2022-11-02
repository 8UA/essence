from googlesearch import search
from linecache import getline
import urllib.request as ul
from bs4 import BeautifulSoup as soup
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


query = input('Search -> ')
print("Searching...\n")


"""
Using the googlesearch module to search for results
and making a file listing all the urls.
"""

results = open('results.temp', 'w', encoding=enctype)

for j in search(query, tld="co.in", num=numpages, stop=numpages):
    results.write(f'{j}\n')

results.close()


"""
Printing each individual url from file
with corresponding numbers.
"""

page_num = 0
with open('results.temp') as file:
    for line in file:
        page_num += 1
        print(f'{page_num} | {line.rstrip()}\n')


"""
Getting the number of the page from user input 
and showing the selected url.
"""

while True:
    try:
        page_opt = int(input('Page number > '))
    except ValueError:
        print("Please input the number of a page.")
        continue
    else:
        break

page_opt_url = getline('results.temp', page_opt)
print(page_opt_url)


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
Remove excessive space characters from the scraped text
and print the final result.
"""

finalrender = " ".join(html_text.split())
print(finalrender)
