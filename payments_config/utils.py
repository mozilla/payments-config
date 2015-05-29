import gettext

locales = [
    'ca', 'cs', 'cy', 'da', 'de', 'dsb', 'en', 'es', 'es_AR', 'es_CL',
    'et', 'eu', 'ff', 'fr', 'fy', 'he', 'hsb', 'hu', 'id', 'it', 'ja', 'ko',
    'lt', 'nb_NO', 'nl', 'pa', 'pl', 'pt', 'pt_BR', 'rm', 'ru', 'sk', 'sl',
    'sq', 'sr', 'sr_Latn', 'sv', 'sv_SE', 'tr', 'uk', 'zh_CN', 'zh_TW'
]


class wrapper(object):
    """
    Wrap translated strings so they can be identified by the encoder.
    """

    def __init__(self, msg):
        self.msg = msg

    def __repr__(self):
        return gettext.gettext(self.msg)
