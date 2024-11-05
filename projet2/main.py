from app.code_scrap_book import iterate_categories_print_all_books_pictures

def main():
    url = "http://books.toscrape.com/index.html"
    iterate_categories_print_all_books_pictures(url)

if __name__ == "__main__":
    main()