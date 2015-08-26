from decimal import Decimal

import babel
from babel import numbers

from products import config
from payments_config.utils import ready_locales

products = {}
sellers = {}


class Seller(object):
    required = ['kind', 'name', 'products']

    def __init__(self, id, config):
        self.id = id

        for k in self.required:
            if k not in config:
                raise ValueError('Missing {} on seller'.format(k))

        for k, v in config.items():
            setattr(self, k, v)

        self.products = [Product(self, p) for p in config['products']]

        if self.kind not in ['products', 'donations']:
            raise ValueError('Unknown kind of seller: {}'.format(self.kind))

    def to_dump(self):
        # Remove the products when dumping the seller, since the
        # products will be dumped seperately.
        data = self.__dict__.copy()
        data.pop('products')
        return data


class Product(object):
    required = ['id', 'description', 'recurrence', 'user_identification']
    valid_user_identifications = ['fxa-auth', 'email', None]

    def __init__(self, seller, config):
        self.amount = None
        self.active = True
        self.currency = 'USD'
        self.seller = seller
        self.recurrence = None
        self.img = ('https://raw.githubusercontent.com/mozilla'
                    '/payments-config/master/payments_config'
                    '/assets/default.png')

        for k in self.required:
            if k not in config:
                raise ValueError('Missing {} on product'.format(k))

        for k, v in config.items():
            setattr(self, k, v)

        self.id = seller.id + '-' + config['id']

        if self.recurrence and self.recurrence not in ['monthly']:
            raise ValueError('Recurrence should be not set or monthly: {}'.
                             format(self.recurrence))

        if (self.user_identification not in self.valid_user_identifications):
            raise ValueError('user_identification must be one of: {}'.
                             format(self.valid_user_identifications))

        if self.amount:
            self.amount = Decimal(self.amount)

        self.price = self.format_prices(ready_locales)

    def format_prices(self, locales):
        prices = {}
        if not self.amount:
            return prices

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


def populate(configuration):
    """
    Returns two dictionaries of sellers and products populated by the
    configuration.
    """
    seller_store, product_store = {}, {}
    for key, seller in configuration.items():
        seller_obj = Seller(key, seller)

        seller_store[seller_obj.id] = seller_obj
        for product_obj in seller_obj.products:
            # Check ids are unique.
            if product_obj.id in product_store:
                raise ValueError(
                    'Repeated product uid: {}'.format(product_obj.id))

            product_store[product_obj.id] = product_obj

    return seller_store, product_store

if not sellers and not products:
    sellers, products = populate(config)
