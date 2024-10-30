import requests
from bs4 import BeautifulSoup
from classe import Book 
import csv
import re

book_url = "http://books.toscrape.com/catalogue/its-only-the-himalayas_981/index.html"
response = requests.get(book_url)

# Vérifie que la requête est réussie
if response.status_code == 200:
    response.encoding = 'utf-8'
    # Étape 2 : Parse le contenu HTML
    soup_client = BeautifulSoup(response.text, 'html.parser')

    #Title bloc
    product_title_div = soup_client.find("div", class_="col-sm-6 product_main")
    #Title field
    if product_title_div:
        h1_tag = product_title_div.find("h1")
        if h1_tag:
            title_value = h1_tag.get_text(strip=True)
        else:
            title_value = None

        #Number available field
        number_available_tag = product_title_div.find("p", class_="instock availability")
        if number_available_tag:
            number_available_string = number_available_tag.get_text(strip=True)
            match = re.search(r"\((\d+)", number_available_string)
            if match:
                number_available = int(match.group(1))
            else:
                number_available = None
        else:
            number_available = None
        #rating star field
        star_rating_tag = soup_client.find("p", class_="star-rating")

        if star_rating_tag:
            # Récupère toutes les classes et filtre celle qui suit "star-rating"
            star_rating_classes = star_rating_tag["class"]
            rating_word = next((cls for cls in star_rating_classes if cls != "star-rating"), None)
            
            # Dictionnaire pour convertir le mot en chiffre
            word_to_number = {
                "Zero": 0,
                "One": 1,
                "Two": 2,
                "Three": 3,
                "Four": 4,
                "Five": 5
            }
            
            # Convertit en chiffre si le mot est dans le dictionnaire
            rating_number = word_to_number.get(rating_word, None)
        else:
            rating_number = None
    else:
        rating_number = None
        title_value = None
        number_available = None

    #Description bloc
    product_page_article = soup_client.find("article", class_="product_page")
    
    if product_page_article:
        # Trouve la première balise <p> à l'intérieur de l'article
        desc_tag = product_page_article.find("p", recursive=False)
        if desc_tag:
            # Récupère le texte de la balise <p>
            desc_text = desc_tag.get_text(strip=True)
        else:
            desc_text = None
    #Table bloc
    table_data = soup_client.find("table", class_="table table-striped")
    rows = table_data.find_all("tr")  
    for row in rows:
        th = row.find("th")
        td = row.find("td")
        name = th.get_text(strip=True)
        value = td.get_text(strip=True)
        if name =='UPC':
            upc_value = value
        elif name == 'Price (incl. tax)':
            price_including_tax = float(value.replace('£', '').strip().replace(',', '.'))
        elif name == 'Price (excl. tax)':
            price_excluding_tax = float(value.replace('£', '').strip().replace(',', '.'))

    #Category bloc
    breadcrumb_ul = soup_client.find("ul", class_="breadcrumb")
    if breadcrumb_ul:
        # Récupère tous les éléments <li> dans la liste
        li_items = breadcrumb_ul.find_all("li")
        if len(li_items) >= 2:
            # Récupère le troisième <li>
            third_li = li_items[2]  # Indice 2 pour la troisième <li>
            
            # Récupère le texte du lien <a> dans le troisième <li>
            a_tag = third_li.find("a")
            if a_tag:
                categ_text = a_tag.get_text(strip=True)
            else:
                categ_text = None
    #image bloc
    image_div = soup_client.find("div", class_="item active")
    if image_div:
        image_tag = image_div.find("img")
        if image_tag:
            image_url = image_tag["src"].replace('../..', 'http://books.toscrape.com/')
        else:
            image_url = None

    # Étape 3 : Crée un objet de la classe Book
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
    # Étape 4 : imprimez les informations du livre dans un csv 
    with open("book_data.csv", "w", newline="") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(book.__dict__.keys())
        csv_writer.writerow(book.__dict__.values())



    


        
