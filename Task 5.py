import requests
from bs4 import BeautifulSoup
import csv

# URL of the e-commerce website (Example: Amazon or Flipkart)
URL = 'https://example.com/products'

# Headers to mimic a browser visit
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    'Accept-Language': 'en-US, en;q=0.5'
}

# Function to get HTML content
def get_page_content(url):
    response = requests.get(url, headers=HEADERS)
    return response.content

# Function to parse product data
def parse_products(content):
    soup = BeautifulSoup(content, 'html.parser')
    products = []

    # Modify the selectors based on the target website's structure
    items = soup.find_all('div', class_='product-item')
    for item in items:
        name = item.find('h2', class_='product-title').text.strip()
        price = item.find('span', class_='product-price').text.strip()
        rating = item.find('span', class_='product-rating').text.strip() if item.find('span', class_='product-rating') else 'No rating'

        products.append({
            'Name': name,
            'Price': price,
            'Rating': rating
        })

    return products

# Function to save data into CSV
def save_to_csv(products):
    with open('products.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['Name', 'Price', 'Rating'])
        writer.writeheader()
        for product in products:
            writer.writerow(product)

# Main function
def main():
    print('Fetching data...')
    content = get_page_content(URL)
    products = parse_products(content)
    save_to_csv(products)
    print('Data saved to products.csv')

if __name__ == '__main__':
    main()
