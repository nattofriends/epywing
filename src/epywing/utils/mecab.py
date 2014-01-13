# -*- coding: utf-8 -*-

from collections import namedtuple
import re
import string

import MeCab
from textblob import TextBlob
from unidecode import unidecode

class MecabToken(namedtuple('MecabToken', ['surface', 'pos', 'type', 'reading'])):
    INELIGIBLE_POS = (u'助詞',)
    VERB = u'動詞'
    AUX_VERB = u'助動詞'
    TE = (u'て', u'で')
    MORPHEME_TYPE_NOT_RECOGNIZED = '1'

    @property
    def eligible(self):
        return self.pos not in MecabToken.INELIGIBLE_POS


class MecabTokenizer(object):
    def __init__(self):
        self.mecab = MeCab.Tagger("--node-format=%m```%f[0]```%s```%f[6]\\n --eos-format=")

    def split(self, text):
        parse_result = self.mecab.parse(text.encode('utf8')).decode('utf8').split('\n')[:-1]
        tagged = [MecabToken(*token.split('```')) for token in parse_result]
        # Time to do some not-altogether-correct things
        ja_tagged = []
        for token in tagged:
            if token.type != MecabToken.MORPHEME_TYPE_NOT_RECOGNIZED:
                last = ja_tagged[-1] if any(ja_tagged) else None
                if last and last.pos == MecabToken.VERB and (token.pos == MecabToken.AUX_VERB or token.surface in MecabToken.TE):
                    ja_tagged[-1] = last._replace(surface=last.surface + token.surface)
                else:
                    ja_tagged.append(token)
        return ja_tagged


class TextBlobToken(namedtuple('TextBlobToken', ['surface', 'pos', 'reading'])):
    INELIGIBLE_POS = (u'DT',)
    INELIGIBLE_SURFACE = (u'sth', u'sb') + tuple(string.ascii_letters)
    @property
    def eligible(self):
        return self.pos not in TextBlobToken.INELIGIBLE_POS and self.surface not in TextBlobToken.INELIGIBLE_SURFACE


class TextBlobTokenizer(object):
    def split(self, text):
        text = text.encode('ascii', 'ignore')
        # text = re.sub(ur'[\u3000-\u30ff\u4e00-\u9fff\ufe30-\ufe4f\uff00-\uffef]+', u'', text)
        # decoded_text = unidecode(text)
        blob = TextBlob(text)
        tagged = blob.tags
        # No English lemmatization support for now
        return [TextBlobToken(*token + (token[0],)) for token in tagged]
