[![Build Status](https://travis-ci.org/mozilla/payments-config.svg?branch=0.0.4)](https://travis-ci.org/mozilla/payments-config)
[![npm version](https://badge.fury.io/js/mozilla-payments-config.svg)](http://badge.fury.io/js/mozilla-payments-config)
[![PyPI version](https://badge.fury.io/py/payments-config.svg)](http://badge.fury.io/py/payments-config)

# Payments Config

Configuration of products for payments-service, solitude et al.

`python generate.py` creates translations and json files.

In Python:

```
>>> from payments_config import products
>>> products['mozilla-concrete-brick'].amount
Decimal('10.00')
```

In Node:

```
> fs = require('fs')
> fs.readFile('json/products/mozilla-concrete-brick.json', 'utf-8', function(err, data) { console.log(JSON.parse(data).amount) });
> 10.00
```

## Making a release

* Bump the version in `package.json`
* Commit and push to master
* Go to the [releases page](https://github.com/mozilla/payments-config/releases)
  and make a new release using the version e.g. 0.0.4 for the tag and Release
  title.
* Travis will automagically make releases on PyPi and npm for you.
