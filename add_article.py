url = input("URL of article: ")
date = input("Date of article: ")
custom_title = input("Custom title of article: ")
preview = input("The beginning text of the article: ")

done = str(f"<a href=\"{url}\" title=\"{date} {preview}\">{custom_title}</a>")

print(done)

kind = input("Would you like to add it to the page now? If so, which? (or type \"no\") ")
if kind == 'no':
    exit()

categories = [
    "header",
    "voiceless",
    "servants",
    "creation",
    "other"
]

filenames = [
    "0-header.txt",
    "1-voiceless.txt",
    "2-servants.txt",
    "3-creation.txt",
    "4-other.txt"
]


for x in range(0, len(categories)):
    if categories[x] == kind:
        with open('data/' + filenames[x], 'r') as file:
            current = file.readlines()
        
        newcontents = current + [done]

        with open('data/' + filenames[x], 'w') as file:
            file.write(''.join(newcontents))

        print("Saved into " + 'data/' + filenames[x])
