from potato.conf import settings

def calculate_price(
    grams: float,
) -> float:
    """
    calculate the price of potatoes based on wight

    Parameters:
        grams: weight of potatoes in grams
    """
    
    if grams >= settings.discount_threashold_grams:
        return (grams / 100) * settings.price_100g_discounted
    else:
        return (grams / 100) * settings.price_100g
    