from decimal import Decimal

from products import config


products = {}
sellers = {}


class Seller(object):

    def __init__(self, id, config):
        self.id = id
        self.products = [Product(self.id, p) for p in config.pop('products')]

        # Check ids are unique.
        if self.id in sellers:
            raise ValueError('Repeated seller uid: {}'.format(self.id))

        for k, v in config.items():
            setattr(self, k, v)

        sellers[self.id] = self

    def to_dump(self):
        data = self.__dict__.copy()
        data.pop('products')
        return data


class Product(object):

    def __init__(self, id, config):
        # Provide some defaults.
        self.active = True
        self.currency = 'USD'
        self.img = ('https://raw.githubusercontent.com/mozilla'
                    '/payments-config/master/config/assets/brick.png')

        self.id = id + '-' + config.pop('id')

        # Check ids are unique.
        if self.id in products:
            raise ValueError('Repeated product uid: {}'.format(self.id))

        for k, v in config.items():
            setattr(self, k, v)

        self.amount = Decimal(self.amount)
        products[self.id] = self

    def to_dump(self):
        return self.__dict__


if not products and not sellers:
    for key, seller in config.items():
        Seller(key, seller)
