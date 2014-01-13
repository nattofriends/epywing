# -*- coding: utf-8 -*-

from collections import namedtuple

import MeCab
from textblob import TextBlob

class MecabToken(namedtuple('MecabToken', ['surface', 'pos', 'type'])):
    INELIGIBLE_POS = (u'助詞',)
    MORPHEME_TYPE_NOT_RECOGNIZED = '1'
    @property
    def eligible(self):
        return self.type != MecabToken.MORPHEME_TYPE_NOT_RECOGNIZED \
                and self.pos not in MecabToken.INELIGIBLE_POS


class MecabTokenizer(object):
    def __init__(self):
        self.mecab = MeCab.Tagger("--node-format=%m```%f[0]```%s\\n --eos-format=")

    def split(self, text):
        parse_result = self.mecab.parse(text.encode('utf8')).decode('utf8').split('\n')[:-1]
        return [MecabToken(*token.split('```')) for token in parse_result]


class TextBlobToken(namedtuple('TextBlobToken', ['surface', 'pos'])):
    INELIGIBLE_POS = (u'DT',)
    @property
    def eligible(self):
        return self.pos not in TextBlobToken.INELIGIBLE_POS


class TextBlobTokenizer(object):
    def split(self, text):
        blob = TextBlob(text)
        tagged = blob.tags
        # It's highly unlikely that any of these English words will have
        # Unicode. Sorry, bub.
        en_tagged = []
        for token in tagged:
            try:
                token[0].decode('ascii')
                en_tagged.append(token)
            except UnicodeEncodeError:
                pass
        return [TextBlobToken(*token) for token in en_tagged]
