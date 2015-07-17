from utils import wrapper as _


config = {
    # Concrete is Mozilla's example site.
    'mozilla-concrete': {
        'name': {
            'en': 'Mozilla Concrete'
        },
        'email': 'support@concrete.mozilla.org',
        'url': 'http://pay.dev.mozaws.net/',
        'terms': 'http://pay.dev.mozaws.net/terms/',
        'products': [
            {
                'id': 'brick',
                'description': {
                    'en': 'Brick'
                },
                'amount': '10.00',
            },
            {
                'id': 'mortar',
                'description': {
                    'en': 'Mortar'
                },
                'amount': '5.00',
                'img': ('https://raw.githubusercontent.com/mozilla'
                        '/payments-config/master/payments_config'
                        '/assets/mortar.png'),
            }
        ]
    }
}
