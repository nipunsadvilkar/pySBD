# -*- coding: utf-8 -*-
from pysbd.abbreviation_replacer import AbbreviationReplacer
from pysbd.lang.common import Common, Standard

class Polish(Common, Standard):

    iso_code = 'pl'

    class AbbreviationReplacer(AbbreviationReplacer):
        SENTENCE_STARTERS = []

    class Abbreviation(Standard.Abbreviation):
        ABBREVIATIONS = ['ags', 'alb', 'ang', 'aor', 'awest', 'bałt', 'bojkow', 'bret', 'brus', 'bsł', 'bułg', 'c.b.d.o', 'c.b.d.u', 'celt', 'chorw', 'cs', 'czakaw', 'czerw', 'czes', 'dłuż', 'dniem', 'dor', 'dubrow', 'duń', 'ekaw', 'fiń', 'franc', 'gal', 'germ', 'głuż', 'gniem', 'goc', 'gr', 'grudz', 'hebr', 'het', 'hol', 'I cont', 'ie', 'ikaw', 'irań', 'irl', 'islandz', 'itd', 'itd.', 'itp', 'jekaw', 'kajkaw', 'kasz', 'kirg', 'kwiec', 'łac', 'lip', 'listop', 'lit', 'łot', 'lp', 'maced', 'mar', 'młpol', 'moraw', 'n.e', 'nb.', 'ngr', 'niem', 'nord', 'norw', 'np', 'np.', 'ok.', 'orm', 'oset', 'osk', 'p.n', 'p.n.e', 'p.o', 'pazdz', 'pers', 'pie', 'pod red.', 'podhal', 'pol', 'połab', 'port', 'prekm', 'pskow', 'psł', 'R cont', 'rez', 'rom', 'rozdz.', 'rum', 'rus', 'rys.', 'sas', 'sch', 'scs', 'serb', 'sierp', 'śl', 'sła', 'słe', 'słi', 'słow', 'sp. z o.o', 'śrdniem', 'śrgniem', 'śrirl', 'stbułg', 'stind', 'stpol', 'stpr', 'str.', 'strus', 'stwniem', 'stycz', 'sztokaw', 'szwedz', 't.', 'tj.', 'tłum.', 'toch', 'tur', 'tzn', 'ukr', 'ul', 'umbr', 'wed', 'węg', 'wlkpol', 'włos', 'wrzes', 'wyd.', 'zakarp']
        PREPOSITIVE_ABBREVIATIONS = []
        NUMBER_ABBREVIATIONS = []
