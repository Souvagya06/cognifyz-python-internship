import requests
from bs4 import BeautifulSoup

def scrape_quotes():
    url = "http://quotes.toscrape.com/"

    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        quotes = soup.find_all("span", class_="text")
        authors = soup.find_all("small", class_="author")

        print("\n--- Quotes ---\n")

        for i in range(len(quotes)):
            print(f"{i+1}. {quotes[i].text}")
            print(f"   - {authors[i].text}\n")

    except requests.exceptions.RequestException:
        print("Error fetching the website!")


# Run scraper
scrape_quotes()