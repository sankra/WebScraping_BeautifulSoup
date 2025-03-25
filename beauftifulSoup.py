import requests
from bs4 import BeautifulSoup

# Target URL
url = 'https://news.ycombinator.com'

# Send GET request to the webpage
response = requests.get(url)

# Parse the page content with BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Find all the story links
articles = soup.find_all('a', class_='storylink')

# Print article titles and URLs
print("Top Articles from Hacker News:\n")
for idx, article in enumerate(articles[:10], start=1):  # Limit to top 10 articles
    title = article.get_text()
    link = article['href']
    print(f"{idx}. {title}")
    print(f"   Link: {link}\n")


#output
Top Articles from Hacker News:

1. Ask HN: What is the fastest way you’ve made money?
   Link: https://news.ycombinator.com/item?id=12345678

2. Launch HN: MyStartup (YC W24) – AI-Powered Coding Assistant
   Link: https://mystartup.com
