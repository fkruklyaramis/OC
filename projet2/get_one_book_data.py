import csv
import re
import requests
from bs4 import BeautifulSoup
from classes import Book
from functions import clean_price

book_url = "http://books.toscrape.com/catalogue/its-only-the-himalayas_981/index.html"
try:
    response = requests.get(book_url)
    response.raise_for_status()
    response.encoding = 'utf-8'

   # Get HTML content 
    soup = BeautifulSoup(response.text, 'html.parser')

    # Titre et stock
    product_main = soup.find("div", class_="col-sm-6 product_main")
    title_value = product_main.find("h1").get_text(strip=True) if product_main else None

    number_available_tag = product_main.find("p", class_="instock availability") if product_main else None
    number_available = int(re.search(r"\((\d+)", number_available_tag.get_text(strip=True)).group(1)) if number_available_tag else None

    # Évaluation en étoiles
    star_rating = soup.find("p", class_="star-rating")
    rating_map = {"Zero": 0, "One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
    rating_number = rating_map.get(next((cls for cls in star_rating["class"] if cls != "star-rating"), None), None) if star_rating else None

    # Description
    desc_tag = soup.find("article", class_="product_page").find("p", recursive=False) if soup.find("article", class_="product_page") else None
    desc_text = desc_tag.get_text(strip=True) if desc_tag else None

    # Données du tableau
    table_data = {row.find("th").get_text(strip=True): row.find("td").get_text(strip=True) for row in soup.find("table", class_="table table-striped").find_all("tr")}
    upc_value = table_data.get("UPC")
    price_including_tax = clean_price(table_data.get("Price (incl. tax)", ""), "pound")
    price_excluding_tax = clean_price(table_data.get("Price (excl. tax)", ""), "pound")

    # Catégorie
    breadcrumb = soup.find("ul", class_="breadcrumb")
    categ_text = breadcrumb.find_all("li")[2].find("a").get_text(strip=True) if breadcrumb and len(breadcrumb.find_all("li")) >= 3 else None

    # URL de l'image
    image_url = soup.find("div", class_="item active").find("img")["src"].replace('../..', 'http://books.toscrape.com/') if soup.find("div", class_="item active") else None

    # Création de l'objet Book
    book = Book(
        product_page_url=book_url,
        universal_product_code=upc_value,
        title=title_value,
        price_including_tax=price_including_tax,
        price_excluding_tax=price_excluding_tax,
        number_available=number_available,
        product_description=desc_text,
        category=categ_text,
        review_rating=rating_number,
        image_url=image_url
    )

    # Enregistrement en CSV
    with open("book_data.csv", "w", newline="") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(book.__dict__.keys())
        csv_writer.writerow(book.__dict__.values())

except requests.RequestException as e:
    print(f"Erreur de requête: {e}")
except Exception as e:
    print(f"Une erreur s'est produite: {e}")