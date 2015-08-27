import copy
import json
import unittest

from generate import Encoder
from payments_config import Seller
from payments_config import populate
from payments_config.utils import wrapper


example_data = {
    'kind': 'products',
    'name': 'example',
    'products': [{
        'amount': '3',
        'currency': 'CAD',
        'description': 'f',
        'id': 'test',
        'recurrence': 'monthly',
        'user_identification': None,
    }],
    'url': 'http://example.com',
}


def example_seller(**kw):
    data = copy.deepcopy(example_data)
    data.update(**kw)
    return Seller('mozilla-concrete', data)


class TestTranslation(unittest.TestCase):

    def test_json(self):
        assert (json.dumps({'key': wrapper('value')}, cls=Encoder) ==
                json.dumps({"key": {"en": "value"}}))


class TestSeller(unittest.TestCase):

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

    def test_kind(self):
        with self.assertRaises(ValueError):
            example_seller(kind='arms-dealer')

    def test_no_amount(self):
        s = example_seller(products=[{
            'description': 'some-description',
            'id': 'no-amount',
            'recurrence': None,
            'user_identification': None,
        }])
        assert s.products[0].amount is None
        assert s.products[0].price == {}

    def test_user_identification_is_valid_option(self):
        with self.assertRaises(ValueError):
            example_seller(products=[{
                'id': 'hai',
                'description': 'a description',
                'recurrence': None,
                'user_identification': True,
            }])

    def test_user_identification_is_required(self):
        with self.assertRaises(ValueError):
            example_seller(products=[{
                'id': 'hai',
                'description': 'a description',
                'recurrence': None,
            }])


class TestRepeats(unittest.TestCase):

    def setUp(self):
        self.data = {'moz': copy.deepcopy(example_data)}
        super(TestRepeats, self).setUp()

    def test_duplicated_product(self):
        self.data['moz']['products'].append(example_data['products'][0])
        with self.assertRaises(ValueError):
            populate(self.data)

    def test_populate(self):
        sellers, products = populate(self.data)
        assert sellers['moz'].kind == 'products'
        assert products['moz-test'].amount == 3


if __name__ == '__main__':
    unittest.main()
