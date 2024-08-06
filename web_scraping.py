import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_books():
    url = "http://books.toscrape.com/"
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "html.parser")

        books = []
        for item in soup.find_all('article', class_='product_pod'):
            title = item.h3.a['title']
            price = item.find('p', class_='price_color').text
            rating_class = item.find('p', class_='star-rating')['class'][1]
            rating = ['One', 'Two', 'Three', 'Four', 'Five'].index(rating_class) + 1
            books.append({'title': title, 'price': float(price[1:]), 'rating': rating})

        return pd.DataFrame(books)
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return pd.DataFrame()
    
if __name__ == "__main__":
    df = scrape_books()
    df.to_csv('books.csv', index=False)