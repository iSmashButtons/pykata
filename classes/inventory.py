# Product Inventory Project: Create an application which manages an inventory of
# products. Create a product class which has a price, id, and quantity on hand.
# Then create an *inventory* class which keeps track of various products and can
# sum up the inventory value.


class Product:
    all = []

    def __init__(name, price, idn, quantity):
        self.__name = name
        self.__price = price
        self.__idn = idn
        self.__quantity = quantity

        Product.all.append(self)

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price