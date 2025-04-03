#sample Code

import requests
from bs4 import BeautifulSoup

#Replace with your url
url = "https://www.geeksforgeeks.org/"
response = requests.get(url)

#checking the status code
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all article title links in the homepage carousel/posts
    titles = soup.select('div.head > a')

    for title in titles:
        text = title.get_text(strip=True)
        href = title.get('href')
        print(f"{text} -> {href}")
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
