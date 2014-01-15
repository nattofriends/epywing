# -*- coding: utf-8 -*-

from epywing.bookfilter import BookFilter
from epywing.titles import KenkyushaShinEiwaDaijiten6, KenkyushaShinWaeiDaijiten5

class Kenkyusha(BookFilter):
    applies_to = [KenkyushaShinEiwaDaijiten6, KenkyushaShinWaeiDaijiten5]

    def filter_heading(self, entry, heading):
        if heading is not None:
            replacements = {
            }

            for find, replace in replacements.items():
                heading = heading.replace(find, replace)
        return heading

    def filter_text(self, entry, text):
        return text

    narrow_gaiji = {
        41272: u'\u00c1',
        41273: u'\u00c9',
        41274: u'\u00cd',
        41275: u'\u00d3',
        41276: u'\u00d1',
        41277: u'\u00dd',
        41278: u'\u00e1',
        41279: u'\u00e9',
        41280: u'\u00ed',
        41281: u'\u00f3',
        41282: u'\u00fa',
        41283: u'\u00fd',

        41284: u'\u00c1',
        41285: u'\u00c9',
        41286: u'\u00cd',
        41287: u'\u00d3',
        41288: u'\u00d1',
        41289: u'\u00dd',
        41290: u'\u00e1',
        41291: u'\u00e9',
        41292: u'\u00ed',
        41293: u'\u00f3',
        41294: u'\u00fa',
        41295: u'\u00fd',

        41297: u'\u01ff',

        41299: u'\u00c1',
        41300: u'\u00c9',
        41301: u'\u00cd',
        41302: u'\u00d3',
        41303: u'\u00d1',
        41304: u'\u00dd',

        41305: u'\u00e1',
        41306: u'\u00e9',
        41307: u'\u00ed',
        41308: u'\u00f3',
        41309: u'\u00fa',

        41319: u'\u00e0',
        41320: u'\u00e8',
        41321: u'\u00ec',
        41322: u'\u00f2',
        41323: u'\u00f9',
        41324: u'\u1ef3',

        41332: u'\u00e0',
        41333: u'\u00e8',
        41334: u'\u00ec',
        41335: u'\u00f2',
        41336: u'\u00f9',
        41337: u'\u1ef3',

        41340: u'\u00c4',
        41341: u'\u00cb',
        41342: u'\u00cf',
        41505: u'\u00d6',
        41506: u'\u00dc',
        41507: u'\u0178',

        41508: u'\u00e4',
        41509: u'\u00eb',
        41510: u'\u00ef',
        41511: u'\u00f6',
        41512: u'\u00fc',
        41513: u'\u00ff',

        41515: u'\u00c2',
        41516: u'\u00ca',
        41517: u'\u00ce',
        41518: u'\u00d4',
        41519: u'\u00db',

        41520: u'\u00e2',
        41521: u'\u00ea',
        41522: u'\u00ee',
        41523: u'\u00f4',
        41524: u'\u00fb',

        41525: u'\u0101',
        41526: u'\u0113',
        41527: u'\u012b',
        41528: u'\u014d',
        41529: u'\u016b',
        41530: u'\u0233',

        41543: u'\u0259\u0301',
        41544: u'\u025a\u0301',
        41545: u'\u025b\u0301',
        41546: u'\u026a\u0301',
        41547: u'\u0254\u0301',
        41548: u'\u028a\u0301',
        41549: u'\u026f\u0301',
        41550: u'\u028f\u0301',
        41551: u'\u0251\u0301',

        41552: u'\u0259\u0300',
        41553: u'\u025a\u0300',
        41554: u'\u025b\u0300',
        41555: u'\u026a\u0300',
        41556: u'\u0254\u0300',
        41557: u'\u028a\u0300',
        41558: u'\u026f\u0300',
        41559: u'\u028f\u0300',
        41560: u'\u0251\u0300',

        41567: u'\u006e\u0303',

        41583: u'\u0259',
        41584: u'\u025a',
        41585: u'\u025b',
        41586: u'\u026a',
        41587: u'\u0254',
        41588: u'\u028a',
        41589: u'\u03b8',
        41590: u'\u00f0',
        41591: u'\u0283',
        41592: u'\u0292',
        41593: u'\u014b',

        41594: u'\u02d0',

        41597: u'\u0074\u0323', # I don't think this is right

        42068: u'\u019a',

        42089: u'\u0064\u0323',

        42107: u'\u0067\u0307',

        42282: u'\u00fe',

        42344: u'\u3016',
        42345: u'\u3017',

        42787: u'\u026b\u0329',
    }

    wide_gaiji = {
        45349: u'\u2015',

        45390: u'\u00e6\u0301',
        45391: u'\u00e6\u0300',
        45392: u'\u00e6\u0301',
        45393: u'\u00e6\u0304',
        45394: u'\u00e6\u0303\u0301',
        45395: u'\u00e6\u0303\u0300',
        45396: u'\u00e6\u0303',
        45397: u'\u00e6',

        45398: u'\u0153\u0301',
        45399: u'\u0153\u0300',
        45400: u'\u0153\u0301',
        45401: u'\u0153\u0303',
        45402: u'\u0153',

        45403: u'\u0276',
    }
