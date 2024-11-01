from typing import Literal

def clean_price(price_string: str, price_type: Literal["pound", "dollar", "euro"]) -> float:
    """Nettoie une chaîne de prix et la convertit en float selon la devise spécifiée.

    Args:
        price_string (str): Chaîne contenant le prix avec un symbole monétaire.
        price_type (Literal["pound", "dollar", "euro"]): Type de devise.

    Returns:
        float: Prix converti en nombre flottant.
    """
    if price_type == "pound":
        return float(price_string.replace('£', '').strip().replace(',', '.'))
    elif price_type == "dollar":
        return float(price_string.replace('$', '').strip().replace(',', '.'))
    elif price_type == "euro":
        return float(price_string.replace('€', '').strip().replace(',', '.'))
