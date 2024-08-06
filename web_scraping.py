import requests
import pandas as pd
from bs4 import BeautifulSoup


def scrape_books() -> pd.DataFrame:
    """
    This function scrapes the book data from the given URL and returns a DataFrame.

    Parameters:
    No parameters are required for this function.

    Returns:
    A pandas DataFrame containing the scraped book data. The DataFrame has two columns: 'title' and 'price'.

    The 'title' column contains the title of the book, and the 'price' column contains the price of the book.
    """
    url = "http://books.toscrape.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    books = []
    for item in soup.find_all('article', class_='product_pod'):
        title = item.h3.a['title']
        price = item.find('p', class_='price_color').text
        books.append({'title': title, 'price': price})

    return pd.DataFrame(books)


if __name__ == '__main__':
    books_df = scrape_books()
    books_df.to_csv('books.csv', index=False)
    print('Books saved to books.csv')
