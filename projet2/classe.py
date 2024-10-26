from pydantic import BaseModel as PydanticBaseModel

# Class Book
class Book(PydanticBaseModel):
    product_page_url: str
    universal_product_code: str
    title : str
    price_including_tax : float
    price_excluding_tax : float
    number_available : int
    product_description : str
    category : str
    review_rating : int
    image_url : str
 