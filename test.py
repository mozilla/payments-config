import json
import unittest

from generate import Encoder
from payments_config.utils import wrapper
from payments_config.version import __version__ as py_version


class TestTranslation(unittest.TestCase):

    def test_json(self):
        assert (json.dumps({'key': wrapper('value')}, cls=Encoder) ==
                json.dumps({"key": {"en": "value"}}))


class TestVersionsInSync(unittest.TestCase):

    def test_versions(self):
        with open('package.json', 'r') as package_json:
            npm_json = package_json.read()
        assert (json.loads(npm_json).get('version') ==
                py_version)


if __name__ == '__main__':
    unittest.main()
