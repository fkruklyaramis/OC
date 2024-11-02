import csv
import os
from typing import Union

def clean_price(price_string: str) -> Union[float, None]:
    """clean price string and return a float

    Args:
        price_string (str): price string

    Returns:
        Union[float, None]: float if price is recognized, None otherwise
    """
    price_string = price_string.strip()
    if '£' in price_string:
        return float(price_string.replace('£', '').strip().replace(',', '.'))
    elif '$' in price_string:
        return float(price_string.replace('$', '').strip().replace(',', '.'))
    elif '€' in price_string:
        return float(price_string.replace('€', '').strip().replace(',', '.'))
    else:
        return None

def print_data_into_csv(filename: str, object_array: list[dict], output_dir: str ):
    """print data array into csv with category name

    Args:
        filename (str): name of the file
        object_array (list[dict]): list of dictionaries
        output_dir (str): output directory
    """
    try:
        os.makedirs(output_dir, exist_ok=True)
        saving_path = os.path.join(output_dir, filename)
        with open(saving_path, mode='w', newline='', encoding='utf-8') as csv_file:
            headers = object_array[0].keys() if object_array else []
            writer = csv.DictWriter(csv_file, fieldnames=headers)
            writer.writeheader()  
            writer.writerows(object_array) 
    except Exception as e:
        print(f"Exception - Function : print_data_into_csv : {e}")
