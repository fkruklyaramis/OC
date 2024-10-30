import requests
from bs4 import BeautifulSoup
from classe import Book 
import csv
import re

site_url = "http://books.toscrape.com/index.html"
# Category choice lower mode
category_choice = "historical fiction"

#HTML request
response = requests.get(site_url)
if response.status_code == 200:
    response.encoding = 'utf-8'
    # Parse HTML category list content
    soup_parser = BeautifulSoup(response.text, 'html.parser')
    nav_list_div = soup_parser.find("ul", class_="nav nav-list")
    ul_list_nav = nav_list_div.find("ul")

    # Get all categories
    for li in ul_list_nav.find_all("li"):
        a_tag = li.find("a")
        if a_tag:
            category_url = a_tag['href']  
            category_name = a_tag.get_text(strip=True).lower()
            # Check if the category is the one we want
            if category_choice == category_name:
                # Get all books from the category
                category_url_choice = site_url.replace("index.html", category_url)
                response = requests.get(category_url_choice)

                if response.status_code == 200:
                    response.encoding = 'utf-8'
                    soup_parser = BeautifulSoup(response.text, 'html.parser')

                    # Get the number of pages in the category
                    number_of_pages = soup_parser.find("li", class_="current").get_text(strip=True)
                    number_of_pages = int(number_of_pages.split(" ")[3])

                    # Get all books from the category
                    for i in range(1, number_of_pages + 1):
                        category_url_page_index = category_url.replace("index.html", f"page-{i}.html")
                        response = requests.get("http://books.toscrape.com/" + category_url_page_index)
                        if response.status_code == 200:
                            response.encoding = 'utf-8'
                            soup_parser = BeautifulSoup(response.text, 'html.parser')
                            article_list = soup_parser.find_all("article", class_="product_pod")
                            # Get all books from the page
                            for article in article_list:
                                print(len(article_list))
                                a_tag = article.find("a")
                                book_url = a_tag['href']
                                book_url = book_url.replace("../../../", "http://books.toscrape.com/catalogue/")
                                book_url = book_url.replace("../", "http://books.toscrape.com/catalogue/")
                                #open each book url per pages
                                response = requests.get(book_url)
                                if response.status_code == 200:
                                    response.encoding = 'utf-8'
                                    soup_parser = BeautifulSoup(response.text, 'html.parser')
                            

                                


