import json
import os
from os import path

from payments_config import products, sellers

root = path.abspath(path.join(path.dirname(__file__)))


def as_json():
    target_dir = path.join(root, 'json')

    for product in products.values():
        target = path.join(target_dir, 'products', product.id)
        open(target + '.json', 'w').write(json.dumps(product.to_dump()))

    for seller in sellers.values():
        target = path.join(target_dir, 'sellers', seller.id)
        open(target + '.json', 'w').write(json.dumps(seller.to_dump()))


def locales():
    filename = path.join(root, 'payments_config/products.py')
    cmd = ('xgettext {} -o locale/templates/LC_MESSAGES/messages.pot'
           .format(filename))
    os.system(cmd)

    for locale in os.listdir(path.join(root, 'locale')):
        if locale == 'templates':
            continue
        filename = path.join(root, 'locale', locale, 'LC_MESSAGES/messages.po')
        cmd = ('msginit --input=locale/templates/LC_MESSAGES/messages.pot '
               '--locale={} --no-translator --output={}'
               .format(locale, filename))
        os.system(cmd)


if __name__ == '__main__':
    as_json()
    locales()
