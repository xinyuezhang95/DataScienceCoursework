from bs4 import BeautifulSoup

with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
print(soup.title)
print(soup.title.name)
print(soup.title.string)
# print(soup.prettify())
# print(soup.p)

all_anchor_tags = soup.find_all(name = "a")
for tag in all_anchor_tags:
    print(tag.getText())
    print(tag.get("href"))

heading = soup.find(name = "h1", id = "name")
print(heading)

section_heading = soup.find(name = "h3", class_ = "heading")
print(section_heading)

company_url = soup.select_one(selector = "p a")
print(company_url)

name = soup.select_one(selector = "#name")
print(name)

heading_class = soup.select(selector = ".heading")
print(heading_class)

attr_value = soup.find("h1")
print(attr_value.get("id"))