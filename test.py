import json
import unittest

from generate import Encoder
from payments_config.utils import wrapper


class TestTranslation(unittest.TestCase):

    def test_json(self):
        assert (json.dumps({'key': wrapper('value')}, cls=Encoder) ==
                json.dumps({"key": {"en": "value"}}))


if __name__ == '__main__':
    unittest.main()
