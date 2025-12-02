def get_product_info(product_id, name, quantity, price):
    """
    Returns product information in a well-formatted string.

    :param product_id: Unique identifier for the product
    :param name: Name of the product
    :param quantity: Quantity available
    :param price: Price of the product
    :return: Formatted product information as a string
    """
    formatted_info = (
        f"Product Information:\n"
        f"---------------------\n"
        f"Product ID : {product_id}\n"
        f"Name       : {name}\n"
        f"Quantity   : {quantity}\n"
        f"Price      : ${price:.2f}"
    )
    return formatted_info


# Example usage:
print(get_product_info("P1001", "Wireless Mouse", 25, 19.99))
