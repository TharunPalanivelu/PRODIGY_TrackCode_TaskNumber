import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd

def get_html(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    response = requests.get(url, headers=headers)
    return response.text

def parse_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    products = []

    for item in soup.find_all('div', {'data-component-type': 's-search-result'}):
        name = item.h2.text.strip()
        try:
            price = item.find('span', 'a-price-whole').text.strip() + item.find('span', 'a-price-fraction').text.strip()
        except AttributeError:
            price = None
        try:
            rating = item.i.text.strip()
        except AttributeError:
            rating = None

        products.append({
            'Name': name,
            'Price': price,
            'Rating': rating
        })

    return products

def save_to_csv(data, filename):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False, encoding='utf-8')

def main():
    url = 'https://www.amazon.in/s?k=iqoo+mobile&rh=n%3A1389401031&ref=nb_sb_noss'
    html = get_html(url)
    products = parse_html(html)
    save_to_csv(products, 'amazon_products.csv')

if __name__ == '__main__':
    main()
