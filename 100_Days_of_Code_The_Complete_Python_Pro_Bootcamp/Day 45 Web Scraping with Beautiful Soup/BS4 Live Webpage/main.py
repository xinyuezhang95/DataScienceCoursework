from bs4 import BeautifulSoup
import requests


# Live Website (will change over time)
response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text

# print(yc_web_page)

soup = BeautifulSoup(yc_web_page, "html.parser")
# article_tag_test = soup.find("td", class_ = "title")
# print(article_tag_test)

articles = soup.find_all("td", class_ = "title")
article_texts = []
article_links = []
for article_tag in articles:
    if article_tag.find("a"):
        text = article_tag.find("a").getText()
        article_texts.append(text)
        link = article_tag.find(name='a').get("href")
        article_links.append(link)

# Finding the upvotes
# If all articles on the page have upvotes, this will work:
# article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

# However, some submissions may not have any upvotes yet.
# This uses a conditional expression to handle cases where there are no upvotes (span is None)
subtexts = soup.findAll(class_="subtext")
article_upvotes = [int(line.span.span.getText().strip(" points")) if line.span.span else 0 for line in subtexts]

largest_number = max(article_upvotes)
largest_index = article_upvotes.index(largest_number)

print(
    f"Most upvoted article: {article_texts[largest_index]}\n"
    f"Number of upvotes: {article_upvotes[largest_index]} points\n"
    f"Available at: {article_links[largest_index]}."
)