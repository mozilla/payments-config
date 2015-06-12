import json
from setuptools import find_packages, setup


def get_version():
    """
    Return package version as in package.json.
    """
    return json.load(open('package.json', 'r'))['version']


setup(
    name='payments-config',
    version=get_version(),
    description='Payments Configuration',
    author='Andy McKay',
    author_email='andym@mozilla.com',
    license='BSD',
    packages=find_packages(),
    install_requires=('babel'),
    url='https://github.com/andymckay/payments-config',
    zip_safe=False,
)
