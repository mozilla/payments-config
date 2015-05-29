from utils import wrapper as _


config = {
    # Concrete is Mozilla's example site.
    'mozilla-concrete': {
        'url': 'http://pay.dev.mozaws.net/',
        'terms': 'http://pay.dev.mozaws.net/terms/',
        'products': [
            {
                'id': 'brick',
                'description': _('Such a fine brick'),
                'amount': '10.00',
            },
            {
                'id': 'mortar',
                'description': _('Some mortar'),
                'amount': '5.00',
                'img': ('https://raw.githubusercontent.com/mozilla'
                        '/payments-config/master/config/assets/mortar.png'),
            }
        ]
    }
}
