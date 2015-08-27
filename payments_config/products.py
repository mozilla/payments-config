from utils import wrapper as _


config = {
    # Concrete is Mozilla's example site.
    'mozilla-concrete': {
        'email': 'support@concrete.mozilla.org',
        'name': _('Mozilla Concrete'),
        'url': 'http://pay.dev.mozaws.net/',
        'terms': 'http://pay.dev.mozaws.net/terms/',
        'kind': 'products',
        'products': [
            {
                'id': 'brick',
                'description': _('Brick'),
                'amount': '10.00',
                # Currently, recurrence infers authentication.
                'recurrence': 'monthly',
                'user_identification': 'fxa-auth',
            },
            {
                'id': 'mortar',
                'description': _('Mortar'),
                'amount': '5.00',
                'img': ('https://raw.githubusercontent.com/mozilla'
                        '/payments-config/master/payments_config'
                        '/assets/mortar.png'),
                'recurrence': 'monthly',
                'user_identification': 'fxa-auth',
            }
        ]
    },
    'mozilla-foundation': {
        'email': 'support@foundation.mozilla.org',
        'name': _('Mozilla Foundation'),
        'url': 'http://pay.dev.mozaws.net/',
        'terms': 'http://pay.dev.mozaws.net/terms/',
        'kind': 'donations',
        'products': [
            {
                # A single purchase with a variable amount, no authentication.
                'id': 'donation',
                'description': _('Donation'),
                'recurrence': None,
                'user_identification': None,
            },
            {
                # A recurring donation with a variable amount.
                # Email address required.
                'id': 'recurring-donation',
                'description': _('Recurring Donation'),
                'recurrence': 'monthly',
                'user_identification': 'email',
            }

        ]
    },
}
