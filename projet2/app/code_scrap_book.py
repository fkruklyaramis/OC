import re
import requests
from bs4 import BeautifulSoup
from app.classes import Book
from app.functions import clean_price,print_data_into_csv

def get_data_book(book_url: str):
    try:
         # HTML request & parsing
        response = requests.get(book_url)
        response.raise_for_status()
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'html.parser')

        # Title and stock
        product_main = soup.find("div", class_="col-sm-6 product_main")
        title_value = product_main.find("h1").get_text(strip=True) if product_main else None
        number_available_tag = product_main.find("p", class_="instock availability") if product_main else None
        number_available = int(re.search(r"\((\d+)", number_available_tag.get_text(strip=True)).group(1)) if number_available_tag else None
        # stars rating
        star_rating = soup.find("p", class_="star-rating")
        rating_map = {"Zero": 0, "One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
        rating_number = rating_map.get(next((cls for cls in star_rating["class"] if cls != "star-rating"), None), None) if star_rating else None
        # description
        desc_tag = soup.find("article", class_="product_page").find("p", recursive=False) if soup.find("article", class_="product_page") else None
        desc_text = desc_tag.get_text(strip=True) if desc_tag else None
        # data table
        table_data = {row.find("th").get_text(strip=True): row.find("td").get_text(strip=True) for row in soup.find("table", class_="table table-striped").find_all("tr")}
        upc_value = table_data.get("UPC")
        price_including_tax = clean_price(table_data.get("Price (incl. tax)", ""))
        price_excluding_tax = clean_price(table_data.get("Price (excl. tax)", ""))
        # categoty
        breadcrumb = soup.find("ul", class_="breadcrumb")
        categ_text = breadcrumb.find_all("li")[2].find("a").get_text(strip=True) if breadcrumb and len(breadcrumb.find_all("li")) >= 3 else None
        # image url
        image_url = soup.find("div", class_="item active").find("img")["src"].replace('../..', 'http://books.toscrape.com/') if soup.find("div", class_="item active") else None

        # create book object
        book = Book(
            product_page_url=book_url,
            universal_product_code=upc_value,
            title=title_value.replace("/",""),
            price_including_tax=price_including_tax,
            price_excluding_tax=price_excluding_tax,
            number_available=number_available,
            product_description=desc_text,
            category=categ_text,
            review_rating=rating_number,
            image_url=image_url
        )
        #save image
        book.save_image("./pictures")
        return book

    except requests.RequestException as e:
        print(f"Request exception : {e}")
    except Exception as e:
        print(f"Exception - Function : get_data_book :  {e}")

def iterate_categories_print_all_books_pictures(site_url: str):
    try: 
        # HTML request & parsing
        response = requests.get(site_url)
        response.raise_for_status()
        soup_parser = BeautifulSoup(response.text, 'html.parser')
        nav_list_div = soup_parser.find("ul", class_="nav nav-list").find("ul")

        # iterate over all categories
        for li in nav_list_div.find_all("li"):
            book_object_array = []
            category_url = site_url.replace("index.html", li.find("a")['href']) if (a_tag := li.find("a")) else None
            category_name = a_tag.get_text(strip=True) if a_tag else None
            response = requests.get(category_url)
            response.raise_for_status()
            soup_parser = BeautifulSoup(response.text, 'html.parser')

            # get the number of pages 
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
                    #append book object to dict into array 
                    book_object_array.append(get_data_book(book_url).model_dump())

            #print data array into csv with category name
            print(f"Printing data into csv for category : {category_name}")
            print_data_into_csv(f"{category_name}.csv", book_object_array, "./csv")  

    except requests.RequestException as e:
        print(f"Request exception : {e}")
    except Exception as e:
        print(f"Exception - Function : iterate_categories_print_all_books : {e}")