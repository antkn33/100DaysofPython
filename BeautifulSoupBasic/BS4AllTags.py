from bs4 import BeautifulSoup


with open("website.html") as file:
    contents = file.read()
soup = BeautifulSoup(contents, "html.parser")

all_a_tags = soup.find_all(name="a")
# print(all_a_tags)

#####
# for tag in all_a_tags:
#     # print(tag.getText()) # get the text of the tag
#     print(tag.get('href')) # attribute of tag, get url

#### 
# find h1 tag with id of name
# heading = soup.find(name="h1", id="name")
# print(heading)

#####
# classes note underscore in class_ 
# section_heading = soup.find(name="h3", class_= "heading")
# print(section_heading.text)

#####
# find with CSS selector
company_url = soup.select_one(selector="p a") # can use soup.select to search for all
print(company_url)

# use selector for an id
name = soup.select_one(selector="#name") # use a # sign in front of id

# selector classes
headings = soup.select(".heading") # selects elemnt with class of heading


