from bs4 import BeautifulSoup as bs 
 
file = open('index.html', 'r',encoding='utf-8') 
html = file.read() 
 
soup = bs(html, 'html.parser') 
 
container = soup.find('div', class_= 'container') 
navigator = container.find('div', class_ = 'navigator-container') 
menu = navigator.find('ul', class_ = 'menu') 
title = menu.find_all('li') 
for i in title: 
    print(i.text) 
 
content = container.find('div', class_='content-container') 
post = content.find_all('div', class_ = 'post') 
for i in post: 
    name = i.find('h1',class_='title') 
    print(name.text) 
 
footer = container.find('div',class_ = 'footer') 
box = footer.find('div', class_= 'box') 
box_content = box.find_all('div', class_= 'box-content') 
for i in box: 
    s = i.find('p',class_ = 'description') 
    print(s.text)