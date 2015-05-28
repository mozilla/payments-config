from decimal import Decimal

products = {
    # Concrete is Mozilla's example site.
    'concrete': {
        'seller': 'mozilla-concrete',
        'products': [
            {
                'id': 'brick',
                'name': 'A fine red brick',
                'amount': Decimal('10'),
                'img': '',
            },
            {
                'id': 'mortar',
                'description': 'Some mortar',
                'amount': Decimal('5'),
                'img': '',
            }
        ]
    }
}
