import json
import unittest

from generate import Encoder
from payments_config import Product
from payments_config.utils import wrapper


class TestTranslation(unittest.TestCase):

    def test_json(self):
        assert (json.dumps({'key': wrapper('value')}, cls=Encoder) ==
                json.dumps({"key": {"en": "value"}}))


class TestPrice(unittest.TestCase):

    def test_prices(self):
        p = Product('test', {'id': 'test', 'amount': '3', 'currency': 'CAD'})
        assert (
            p.format_prices(['en', 'tr', 'foopy']) ==
            {'en': u'CA$3.00', 'tr': u'3,00\xa0CA$'}
        )


if __name__ == '__main__':
    unittest.main()
