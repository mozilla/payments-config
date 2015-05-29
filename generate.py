import decimal
import gettext
import json
import os
from os import path

from payments_config import products, sellers
from payments_config.utils import locales, wrapper


root = path.abspath(path.join(path.dirname(__file__)))


class Encoder(json.JSONEncoder):

    def default(self, o):
        if isinstance(o, wrapper):
            # Always supply en.
            res = {'en': o.msg}
            for locale in locales:
                try:
                    lang = gettext.translation(
                        'messages', 'locale',
                        languages=[locale])
                except IOError:
                    continue
                res[locale] = lang.gettext(o.msg)
            return res

        if isinstance(o, decimal.Decimal):
            return str(o)

        return super(self.__class__, self).default(o)


def as_json():
    target_dir = path.join(root, 'json')

    for product in products.values():
        target = path.join(target_dir, 'products', product.id)
        open(target + '.json', 'w').write(
            json.dumps(product.to_dump(), cls=Encoder, indent=2))

    for seller in sellers.values():
        target = path.join(target_dir, 'sellers', seller.id)
        open(target + '.json', 'w').write(
            json.dumps(seller.to_dump(), cls=Encoder, indent=2))


def generate_po():
    filename = path.join(root, 'payments_config/products.py')
    cmd = ('xgettext {} -o locale/templates/LC_MESSAGES/messages.pot'
           .format(filename))
    os.system(cmd)

    for locale in locales:
        if locale == 'templates':
            continue
        filename = path.join(root, 'locale', locale, 'LC_MESSAGES/messages.po')
        cmd = ('msginit --input=locale/templates/LC_MESSAGES/messages.pot '
               '--locale={} --no-translator --output={}'
               .format(locale, filename))
        os.system(cmd)


if __name__ == '__main__':
    as_json()
