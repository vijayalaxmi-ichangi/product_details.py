from product_details import get_product_info   # make sure your file name is product_details.py

def test_get_product_info():
    result = get_product_info("P1001", "Wireless Mouse", 25, 19.99)

    expected = (
        "Product Information:\n"
        "---------------------\n"
        "Product ID : P1001\n"
        "Name       : Wireless Mouse\n"
        "Quantity   : 25\n"
        "Price      : $19.99"
    )

    assert result == expected


