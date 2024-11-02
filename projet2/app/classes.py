import requests
import os
from pydantic import BaseModel as PydanticBaseModel
from typing import Optional

# object book
class Book(PydanticBaseModel):
    product_page_url: str
    universal_product_code: str
    title : str
    price_including_tax : float
    price_excluding_tax : float
    number_available : Optional[int]
    product_description : Optional[str]
    category : str
    review_rating : Optional[int]
    image_url : str

    # save image method
    def save_image(self, output_dir: str):
        """download and save image from the url

        Args:
            output_dir (str): output directory
        """
        try :
            response = requests.get(self.image_url)
            response.raise_for_status()
            os.makedirs(output_dir, exist_ok=True)
            with open(f"{output_dir}/{self.universal_product_code}_{self.title}.jpg", 'wb') as file:
                file.write(response.content)
        except requests.RequestException as e:
            print(f"Request exception - Method : book.save_image : : {e}")