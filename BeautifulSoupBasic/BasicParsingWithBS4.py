from bs4 import BeautifulSoup

with open("website.html") as file:
    contents = file.read()
soup = BeautifulSoup(contents, "html.parser")

print(soup.title)
print(soup.title.name) # name of tag
print(soup.title.string) # string in the tag
print(soup.prettify()) # prints out HTML indented


print(soup.a) # anchor tags

