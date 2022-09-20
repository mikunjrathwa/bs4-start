from bs4 import *
import xml


with open('website.html', encoding="utf8") as html_file:
    html_string = html_file.read()

soup = BeautifulSoup(html_string, 'html.parser')
#print(soup.title)
#print(soup.title.name)
#print(soup.prettify())


#print(soup.findAll('p'))
#print(soup.find(name='h1', id='name'))
#print(soup.find(name='h3', class_='heading'))


print(soup.select('a'))
print(soup.select_one('#name'))
print(soup.select_one('.heading'))