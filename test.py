import json
import unittest

from generate import Encoder
import payments_config
from payments_config import Seller
from payments_config.utils import wrapper


def example_seller(**kw):
    data = {
        'url': 'http://example.com',
        'name': 'example',
        'products': [
            {'id': 'test', 'amount': '3', 'currency': 'CAD'}
        ]
    }
    data.update(**kw)
    return Seller('mozilla-concrete', data)


class TestTranslation(unittest.TestCase):

    def test_json(self):
        assert (json.dumps({'key': wrapper('value')}, cls=Encoder) ==
                json.dumps({"key": {"en": "value"}}))


class TestSeller(unittest.TestCase):

    def setUp(self):
        payments_config.products = {}
        payments_config.sellers = {}

    def test_prices(self):
        s = example_seller()
        assert (
            s.products[0].format_prices(['en', 'tr', 'foopy']) ==
            {'en': u'CA$3.00', 'tr': u'3,00\xa0CA$'}
        )

    def test_seller(self):
        s = example_seller()
        assert s == s.products[0].seller

    def test_dump(self):
        s = example_seller()
        res = s.products[0].to_dump()
        assert s.name == res['seller']['name']


if __name__ == '__main__':
    unittest.main()
