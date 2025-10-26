from potato.conf import settings

def calculate_price(
    grams: float,
) -> int:
    """
    calculate the price of potatoes based on wight

    Parameters:
        grams: weight of potatoes in grams
    """
    
    if grams >= settings.discount_threashold_grams:
        temp = (grams / 100) * settings.price_100g_discounted
    else:
        temp = (grams / 100) * settings.price_100g
    
    return round(int(temp), -1)

    