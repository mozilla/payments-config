Configuration of products for payments-service, solitude et al.

`python generate.py` creates translations and json files.

In Python:

```
>>> from payments_config import products
>>> products['mozilla-concrete-brick'].amount
'10.00'
```

In Node:

```
> fs = require('fs')
> fs.readFile('json/products/mozilla-concrete-brick.json', 'utf-8', function(err, data) { console.log(JSON.parse(data).amount) });
> 10.00
```

TODO:
* get feedback
* build automagically from Travis
* figure out the best format for payments-ui to pull in
