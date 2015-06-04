import os
import re
from setuptools import find_packages, setup


def get_version(package):
    """
    Return package version as listed in `__version__` in `version.py`.
    """
    init_py = open(os.path.join(package, 'version.py')).read()
    return re.search("__version__ = ['\"]([^'\"]+)['\"]", init_py).group(1)


setup(
    name='payments-config',
    version=get_version('payments_config'),
    description='Payments Configuration',
    author='Andy McKay',
    author_email='andym@mozilla.com',
    license='BSD',
    packages=find_packages(),
    url='https://github.com/andymckay/payments-config',
    zip_safe=False,
)
