import csv
import re
import requests
import json
from bs4 import BeautifulSoup
from classes import Book
from functions import clean_price

site_url = "http://books.toscrape.com/index.html"

try: 
    # HTML request & parsing
    response = requests.get(site_url)
    response.raise_for_status()
    soup_parser = BeautifulSoup(response.text, 'html.parser')
    nav_list_div = soup_parser.find("ul", class_="nav nav-list").find("ul")

    # Get all categories
    for li in nav_list_div.find_all("li"):
        category_url = site_url.replace("index.html", li.find("a")['href']) if (a_tag := li.find("a")) else None
        category_name = a_tag.get_text(strip=True) if a_tag else None
        response = requests.get(category_url)
        response.raise_for_status()
        soup_parser = BeautifulSoup(response.text, 'html.parser')

        # Get the number of pages in the category
        if soup_parser.find("ul", class_="pager"):
            number_of_pages = int(soup_parser.find("ul", class_="pager").find("li", class_="current").get_text(strip=True).split(" ")[3])
        else:
            number_of_pages = 1  
        # iterate over all pages
        for i in range(1, number_of_pages + 1):
            category_url_with_index = category_url.replace("index.html", f"page-{i}.html") if number_of_pages > 1 else category_url
            response = requests.get(category_url_with_index)
            response.raise_for_status()
            response.encoding = 'utf-8'
            soup_parser = BeautifulSoup(response.text, 'html.parser')
            book_list = soup_parser.find_all("article", class_="product_pod")
            # Get all books from the page
            for book in book_list:
                book_url = book.find("a")['href'].replace("../../../", "http://books.toscrape.com/catalogue/").replace("../", "http://books.toscrape.com/catalogue/") if book.find("a") else None
                print(book_url)
                # getdatabook
                # init book object
                # ppend data array
        #print data array into csv with category name

                            
except requests.RequestException as e:
    print(f"Erreur de requête: {e}")
except Exception as e:
    print(f"Une erreur s'est produite: {e}")
                                


