import decimal
import gettext
import json
import os
import sys
from os import path

from payments_config import products, sellers
from payments_config.utils import ready_locales, wrapper

root = path.abspath(path.join(path.dirname(__file__)))


class Encoder(json.JSONEncoder):

    def default(self, o):
        if isinstance(o, wrapper):
            # Always supply en.
            res = {'en': o.msg}
            for locale in ready_locales:
                try:
                    lang = gettext.translation(
                        'payments-config', '../payments-l10n/locale',
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


if __name__ == '__main__':
    l10n = os.path.abspath('../payments-l10n')
    if not os.path.exists(l10n):
        print 'Payments l10n not found, looking for it here: ' + l10n
        print '... exiting.'
        sys.exit(1)
    as_json()
