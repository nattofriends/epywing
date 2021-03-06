# -*- coding: utf-8 -*-

from utils.plugin import PluginMount
from epywing.categories import JapaneseEnglish, EnglishJapanese, Japanese


class BookTitle(object):
    '''Base class for book titles.
    '''
    __metaclass__ = PluginMount

    def __init__(self, book, *args, **kwargs):
        self.book = book

    def matches(self):
        ''' Determines whether this classification matches the given EPWING book.
        `self.book` contains the EpwingBook instance.
        '''
        raise NotImplementedError('Subclasses must override this!')

    @classmethod
    def get_title(cls, book):
        '''Returns a subclass instance of BookTitle that identifies the given book instance.
        '''
        for title_class in cls.plugins:
            title = title_class(book)
            if title.matches():
                return title
        return None


# EPWING book titles below

class GeniusEiwaDaijiten(BookTitle):
    label = 'ジーニアス英和大辞典'
    categories = [JapaneseEnglish]

    def matches(self):
        return u'ジーニアス英和大辞典' in self.book.name


class GeniusEiwaWaeiJiten(BookTitle):
    categories = [JapaneseEnglish, EnglishJapanese]

    def matches(self):
        return u'ジーニアス英和・和英辞典' in self.book.name


class SanseidoSuperDaijirin(BookTitle):
    categories = [Japanese, EnglishJapanese]

    def matches(self):
        return u'三省堂　スーパー大辞林' in self.book.name


class Kojien6(BookTitle):
    categories = [Japanese]

    def matches(self):
        return u'広辞苑第六版' in self.book.name


class KenkyushaCollocations(BookTitle):
    #categories = [EnglishJapanese]
    #TODO what category is this, really?

    def matches(self):
        return u'研究社 新編英和活用大辞典' in self.book.name


class KenkyushaShinEiwaDaijiten6(BookTitle):
    categories = [EnglishJapanese]

    def matches(self):
        return u'研究社　新英和大辞典　第６版' in self.book.name


class KenkyushaShinWaeiDaijiten5(BookTitle):
    categories = [JapaneseEnglish]

    def matches(self):
        return u'研究社　新和英大辞典　第５版' in self.book.name


class KenkyushaReadersPlus(BookTitle):
    categories = [EnglishJapanese]

    def matches(self):
        return u'研究社　リーダーズ＋プラス' in self.book.name


