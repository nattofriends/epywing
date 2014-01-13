# -*- coding: utf-8 -*-
from collections import namedtuple

from epywing.bookfilter import BookFilter
from epywing.utils.mecab import MecabTokenizer, TextBlobTokenizer
from epywing.utils.punctuation import punctuation_and_numbers_regex
from lxml import etree, html
import lxml.html
import cgi

# Linkify vocab words that have exact matches in the given entry.

Replacement = namedtuple('Replacement', ['offset', 'start', 'surface', 'search_reading'])

# Use multiple tokenizers for multiple languages.
mecab = MecabTokenizer()
textblob = TextBlobTokenizer()
tokenizers = [mecab, textblob]

# this must be set
book_manager = None


class LinkifyWordsFilter(BookFilter):
    '''This filter turns words in an entry's text into clickable links for searching.
    '''
    #link_template = u'[a href="{url}"]{text}[/a]'
    #link_template = u'<a href="url">{text}</a>'
    link_template = u'<span class="searchable-word" onclick="search({search_reading});">{text}</span>'

    def filter_text(self, entry, text):
        '''`books` is a list of all books to search in when linkifying the entry's text.
        '''
        if hasattr(self.book, 'manager') and self.book.manager is not None:
            self.book_manager = self.book.manager
        else:
            # missing book manager
            return text

        # linkify each text fragment, and put them back together
        html_parser = lxml.etree.HTMLParser()
        root = lxml.html.fromstring(text, parser=html_parser)
        fragments = root.xpath('//text()')

        for fragment in fragments:#self._text_fragments(root):
            # replace the fragment in the etree with the linkified text
            parent = fragment.getparent()

            # don't linkify if it's inside an anchor link tag
            if fragment.is_text and parent.tag == 'a':
                continue

            linkified = self.linkify(cgi.escape(fragment))

            try:
                linkified = etree.XML(u''.join([u'<span>', linkified, u'</span>'])) ##u'<span>' + linkified + u'</span>')#.getroot()#, parser)
            except Exception:
                continue

            if fragment.is_text:
                parent.text = None
                parent.insert(0, linkified)
                # this way is slower, though cleaner since it doesn't insert superfluous <span> tags
                #parent.text = linkified.text
                #for child in reversed(linkified.getchildren()):
                    #parent.insert(0, child)
            else:
                parent.tail = None
                parent.addnext(linkified)
        return etree.tostring(root).decode('utf8')#, encoding='utf8')

    def _exact_match_exists(self, word, _memo={}):
        '''Returns whether there is any exact match in available books.
        '''
        if word in _memo:
            return _memo[word]
        else:
            for book in self.book_manager.books.values():
                if any(book.search(word, search_method='exact')):
                    _memo[word] = True
                    return True
            _memo[word] = False
            return False

    def _is_all_punctuation(self, text, _memo={}):
        '''Returns whether `text` only contains punctuation characters.
        '''
        if text in _memo:
            return _memo[text]
        else:
            _memo[text] = not bool(punctuation_and_numbers_regex.sub(u'', text).strip())
            return _memo[text]

    def linkify(self, text):
        '''
        `text` should not contain any HTML
        '''
        words_by_tokenizer = [tokenizer.split(text) for tokenizer in tokenizers]
        if not any(words_by_tokenizer):
            return text

        # ignore words that might be HTML entries
        #TODO this is required because of a hack
        html_entities = (u'lt', u'gt')
        for i, words in enumerate(words_by_tokenizer):
            words_by_tokenizer[i] = filter(lambda word: word.surface not in html_entities, words)

        link_positions = []
        for words in words_by_tokenizer:
            # find each split word in the original text and linkify if needed
            start = 0
            for index, word in enumerate(words):
                try:
                    offset = text.index(word.surface, start)
                    start = offset + len(word.surface)

                    # only check this word if it's not punctuation
                    if not self._is_all_punctuation(word.surface) \
                    and word.eligible:
                        # match found - we'll add the link later
                        if self._exact_match_exists(word.surface):
                            link_positions.append(Replacement(offset, start, word.surface, word.surface))
                        elif self._exact_match_exists(word.reading):
                            link_positions.append(Replacement(offset, start, word.surface, word.reading))
                except ValueError:
                    continue

        if not link_positions:
            return text

        # when we insert a link, increase the offset by the amount
        # of inserted text, so subsequent link positions are accurate
        offset = 0
        for position in sorted(link_positions):
            from_ = position.offset + offset
            to = position.start + offset
            word = text[from_:to]
            replacement = self.link_template.format(text=position.surface, search_reading=position.search_reading)
            text = u''.join([text[:from_], replacement, text[to:]])
            offset += len(replacement) - len(word)

        return text



