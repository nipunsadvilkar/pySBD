# -*- coding: utf-8 -*-
from pysbd.utils import Rule
from pysbd.abbreviation_replacer import AbbreviationReplacer

class Standard:

    # This class holds the punctuation marks.
    Punctuations = ['。', '．', '.', '！', '!', '?', '？']

    # Rubular: http://rubular.com/r/G2opjedIm9
    GeoLocationRule = Rule(r'(?<=[a-zA-z]°)\.(?=\s*\d+)', '∯')

    FileFormatRule = Rule(r'(?<=\s)\.(?=(jpe?g|png|gif|tiff?|pdf|ps|docx?|xlsx?|svg|bmp|tga|exif|odt|html?|txt|rtf|bat|sxw|xml|zip|exe|msi|blend|wmv|mp[34]|pptx?|flac|rb|cpp|cs|js)\s)', '∯')

    SingleNewLineRule = Rule(r'\n', 'ȹ')

    # Rubular: http://rubular.com/r/aXPUGm6fQh
    QuestionMarkInQuotationRule = Rule(r'\?(?=(\'|\"))', '&ᓷ&')

    ExtraWhiteSpaceRule = Rule(r'\s{3,}', ' ')

    SubSingleQuoteRule = Rule(r'&⎋&', "'")

    class Abbreviation(object):
        """Defines the abbreviations for each language (if available)"""
        ABBREVIATIONS = ['dr.philos', 'dr.phil', 'd.phil', 'messrs', 'attys', 'calif', 'comdr', 'mssrs', 'penna', 'usafa', 'alta', 'ariz', 'assn', 'asst', 'bart', 'bldg', 'blvd', 'brig', 'bros', 'capt', 'cmdr', 'colo', 'conn', 'corp', 'cres', 'dept', 'dist', 'expy', 'hosp', 'hway', 'insp', 'kans', 'mass', 'mich', 'minn', 'miss', 'mlle', 'mont', 'msgr', 'nebr', 'okla', 'penn', 'ph.d', 'prof', 'reps', 'sask', 'sens', 'sept', 'supt', 'surg', 'tenn', 'univ', 'wash', 'wisc', 'adj', 'adm', 'adv', 'ala', 'apr', 'arc', 'ark', 'art', 'aug', 'ave', 'bld', 'btw', 'cal', 'col', 'con', 'cpl', 'dak', 'dec', 'del', 'det', 'drs', 'e.g', 'ens', 'esp', 'esq', 'etc', 'exp', 'ext', 'feb', 'fed', 'fla', 'fwy', 'gen', 'gov', 'hon', 'hwy', 'i.e', 'ida', 'ill', 'inc', 'ind', 'ing', 'jan', 'jul', 'jun', 'kan', 'ken', 'ltd', 'maj', 'man', 'mar', 'may', 'med', 'mex', 'mfg', 'min', 'mme', 'mrs', 'mtn', 'neb', 'nev', 'nos', 'nov', 'oct', 'ont', 'ord', 'ore', 'pde', 'pfc', 'plz', 'pvt', 'que', 'ref', 'rep', 'res', 'rev', 'sec', 'sen', 'sep', 'sfc', 'sgt', 'tce', 'tex', 'u.s', 'ver', 'viz', 'wis', 'wyo', 'yuk', 'fig', 'al', 'cl', 'co', 'ct', 'dr', 'ft', 'fy', 'ga', 'hr', 'ia', 'id', 'is', 'jr', 'ky', 'la', 'lt', 'md', 'me', 'mm', 'mo', 'mr', 'ms', 'mt', 'no', 'nr', 'ok', 'op', 'pa', 'pd', 'ph', 'pl', 'pp', 'rd', 'rs', 'rt', 'sr', 'st', 'ut', 'va', 'vs', 'vt', 'wy', 'p', 'v']
        PREPOSITIVE_ABBREVIATIONS = ['adm', 'attys', 'brig', 'capt', 'cmdr', 'col', 'cpl', 'det', 'dr', 'gen', 'gov', 'ing', 'lt', 'maj', 'mr', 'mrs', 'ms', 'mt', 'messrs', 'mssrs', 'prof', 'ph', 'rep', 'reps', 'rev', 'sen', 'sens', 'sgt', 'st', 'supt', 'v', 'vs', 'fig']
        NUMBER_ABBREVIATIONS = ['art', 'ext', 'no', 'nos', 'p', 'pp']

        # Rubular: http://rubular.com/r/EUbZCNfgei
        # WithMultiplePeriodsAndEmailRule = Rule(r'(\w)(\.)(\w)', '\\1∮\\3')
        # \w in python matches unicode abbreviations also so limit to english alphanumerics
        WithMultiplePeriodsAndEmailRule = Rule(r'([a-zA-Z0-9_])(\.)([a-zA-Z0-9_])', '\\1∮\\3')

    class DoublePunctuationRules(object):
        FirstRule = Rule(r'\?!', '☉')
        SecondRule = Rule(r'!\?', '☈')
        ThirdRule = Rule(r'\?\?', '☇')
        ForthRule = Rule(r'!!', '☄')
        DoublePunctuation = r'\?!|!\?|\?\?|!!'
        All = [FirstRule, SecondRule, ThirdRule, ForthRule]

    class ExclamationPointRules(object):
        # Rubular: http://rubular.com/r/XS1XXFRfM2
        InQuotationRule = Rule(r'\!(?=(\'|\"))', '&ᓴ&')

        # Rubular: http://rubular.com/r/sl57YI8LkA
        BeforeCommaMidSentenceRule = Rule(r'\!(?=\,\s[a-z])', '&ᓴ&')

        # Rubular: http://rubular.com/r/f9zTjmkIPb
        MidSentenceRule = Rule(r'\!(?=\s[a-z])', '&ᓴ&')

        All = [InQuotationRule, BeforeCommaMidSentenceRule, MidSentenceRule]

    class SubSymbolsRules(object):
        Period = Rule(r'∯', '.')
        ArabicComma = Rule(r'♬', '،')
        SemiColon = Rule(r'♭', ':')
        FullWidthPeriod = Rule(r'&ᓰ&', '。')
        SpecialPeriod = Rule(r'&ᓱ&', '．')
        FullWidthExclamation = Rule(r'&ᓳ&', '！')
        ExclamationPoint = Rule(r'&ᓴ&', '!')
        QuestionMark = Rule(r'&ᓷ&', '?')
        FullWidthQuestionMark = Rule(r'&ᓸ&', '？')
        MixedDoubleQE = Rule(r'☉', '?!')
        MixedDoubleQQ = Rule(r'☇', '??')
        MixedDoubleEQ = Rule(r'☈', '!?')
        MixedDoubleEE = Rule(r'☄', '!!')
        LeftParens = Rule(r'&✂&', '(')
        RightParens = Rule(r'&⌬&', ')')
        TemporaryEndingPunctutation = Rule(r'ȸ', '')
        Newline = Rule(r'ȹ', "\n")
        All = [Period, ArabicComma, SemiColon, FullWidthPeriod, SpecialPeriod,
               FullWidthExclamation, ExclamationPoint, QuestionMark,
               FullWidthQuestionMark, MixedDoubleQE, MixedDoubleQQ, MixedDoubleEQ,
               MixedDoubleEE, LeftParens, RightParens, TemporaryEndingPunctutation,
               Newline]

    class EllipsisRules(object):

        # below rules aren't similar to original rules of pragmatic segmenter
        # modification: spaces replaced with same number of symbols
        # Rubular: http://rubular.com/r/i60hCK81fz
        ThreeConsecutiveRule = Rule(r'\.\.\.(?=\s+[A-Z])', '☏☏.')

        # Rubular: http://rubular.com/r/Hdqpd90owl
        FourConsecutiveRule = Rule(r'(?<=\S)\.{3}(?=\.\s[A-Z])', 'ƪƪƪ')

        # Rubular: http://rubular.com/r/YBG1dIHTRu
        ThreeSpaceRule = Rule(r'(\s\.){3}\s', '♟♟♟♟♟♟♟')

        # Rubular: http://rubular.com/r/2VvZ8wRbd8
        FourSpaceRule = Rule(r'(?<=[a-z])(\.\s){3}\.($|\\n)', '♝♝♝♝♝♝♝')

        OtherThreePeriodRule = Rule(r'\.\.\.', 'ƪƪƪ')

        All = [ThreeSpaceRule, FourSpaceRule, FourConsecutiveRule,
               ThreeConsecutiveRule, OtherThreePeriodRule]

    class ReinsertEllipsisRules(object):
        # below rules aren't similar to original rules of pragmatic segmenter
        # modification: symbols replaced with same number of ellipses
        SubThreeConsecutivePeriod = Rule(r'ƪƪƪ', '...')
        SubThreeSpacePeriod = Rule(r'♟♟♟♟♟♟♟', ' . . . ')
        SubFourSpacePeriod = Rule(r'♝♝♝♝♝♝♝', '. . . .')
        SubTwoConsecutivePeriod = Rule(r'☏☏', '..')
        SubOnePeriod = Rule(r'∮', '.')
        All = [SubThreeConsecutivePeriod, SubThreeSpacePeriod, SubFourSpacePeriod,
               SubTwoConsecutivePeriod, SubOnePeriod]

    class AbbreviationReplacer(AbbreviationReplacer):
        SENTENCE_STARTERS = "A Being Did For He How However I In It Millions "\
            "More She That The There They We What When Where Who Why".split(" ")
