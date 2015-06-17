from utils import wrapper as _


config = {
    # Concrete is Mozilla's example site.
    'mozilla-concrete': {
        'name': _('Mozilla Concrete'),
        'url': 'http://pay.dev.mozaws.net/',
        'terms': 'http://pay.dev.mozaws.net/terms/',
        'products': [
            {
                'id': 'brick',
                'description': _('Brick'),
                'amount': '10.00',
            },
            {
                'id': 'mortar',
                'description': _('Mortar'),
                'amount': '5.00',
                'img': ('https://raw.githubusercontent.com/mozilla'
                        '/payments-config/master/payments_config'
                        '/assets/mortar.png'),
            }
        ]
    }
}
