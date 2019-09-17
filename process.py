# This code processes the data in the data directory and combines it with the index.html file
from bs4 import BeautifulSoup
from shutil import copy2

files = [
    "0-header.txt",
    "1-voiceless.txt",
    "2-servants.txt",
    "3-creation.txt",
    "4-other.txt"
]
domID = [
    "header",
    "voiceless",
    "servants",
    "creation",
    "other"
]

# Grab all the information from those above files into the data list
data = {}
for x in range(0, len(files)):
    try:
        with open('data/' + files[x]) as file:
            lines = file.readlines()
    except FileNotFoundError:
        lines = ''
    
    lines = [x.strip() for x in lines]

    data[domID[x]] = lines

    
# Apply to DOM

with open('index.html', 'r') as file:
    website = file.read().replace('\n', '')

website = BeautifulSoup(website, 'lxml')


for element in domID:
    rawdata = ''.join(data[element])
    new_tag = website.new_tag('div')
    temp_soup = BeautifulSoup('<div>' + rawdata + '</div>', 'lxml')
    div_tag = temp_soup.html.body.div
    
    new_tag.string = rawdata
    tag = website.find('div', {'id':element})
    tag.append(div_tag)

    with open("deploy/index.html", "w") as file:
        file.write(str(website))
    

# Now it is time to copy the other files

codefiles = [
    "stylesheet.css",
    "script.js"
]

for document in codefiles:
    copy2(document, 'deploy/')

print("Deployed")
