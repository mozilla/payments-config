from decimal import Decimal

import babel
from babel import numbers

from products import config
from payments_config.utils import ready_locales

products = {}
sellers = {}


class Seller(object):
    required = ['name', 'products']

    def __init__(self, id, config):
        self.id = id

        for k in self.required:
            if k not in config:
                raise ValueError('Missing {} on seller'.format(k))

        for k, v in config.items():
            setattr(self, k, v)

        self.products = [Product(self, p) for p in config.pop('products')]

        # Check ids are unique.
        if self.id in sellers:
            raise ValueError('Repeated seller uid: {}'.format(self.id))

        sellers[self.id] = self

    def to_dump(self):
        # Remove the products when dumping the seller, since the
        # products will be dumped seperately.
        data = self.__dict__.copy()
        data.pop('products')
        return data


class Product(object):

    def __init__(self, seller, config):
        # Provide some defaults.
        self.active = True
        self.currency = 'USD'
        self.seller = seller
        self.img = ('https://raw.githubusercontent.com/mozilla'
                    '/payments-config/master/payments_config'
                    '/assets/default.png')

        self.id = seller.id + '-' + config.pop('id')

        # Check ids are unique.
        if self.id in products:
            raise ValueError('Repeated product uid: {}'.format(self.id))

        for k, v in config.items():
            setattr(self, k, v)

        self.amount = Decimal(self.amount)

        self.price = self.format_prices(ready_locales)

        products[self.id] = self

    def format_prices(self, locales):
        prices = {}
        for locale in locales:
            try:
                prices[locale] = numbers.format_currency(
                    self.amount, self.currency, locale=locale)
            except babel.core.UnknownLocaleError:
                print 'Ignoring unknown locale: {}'.format(locale)
                continue

        return prices

    def to_dump(self):
        # When dumping the product, dump the seller as well, but not the
        # products (removed in seller.to_dump), otherwise you'll be in a
        # recursive mess.
        data = self.__dict__.copy()
        data['seller'] = self.seller.to_dump()
        return data


if not products and not sellers:
    for key, seller in config.items():
        Seller(key, seller)
