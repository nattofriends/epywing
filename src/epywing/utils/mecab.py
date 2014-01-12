# -*- coding: utf-8 -*-

import MeCab

class Wakati(object):
    def __init__(self):
        self.mecab = MeCab.Tagger("-Owakati")

    def split(self, text):
        return self.mecab.parse(text.encode('utf8')).decode('utf8').split()
