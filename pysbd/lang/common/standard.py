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
        ABBREVIATIONS = ['adj', 'adm', 'adv', 'al', 'ala', 'alta', 'apr', 'arc', 'ariz', 'ark', 'art', 'assn', 'asst', 'attys', 'aug', 'ave', 'bart', 'bld', 'bldg', 'blvd', 'brig', 'bros', 'btw', 'cal', 'calif', 'capt', 'cl', 'cmdr', 'co', 'col', 'colo', 'comdr', 'con', 'conn', 'corp', 'cpl', 'cres', 'ct', 'd.phil', 'dak', 'dec', 'del', 'dept', 'det', 'dist', 'dr', 'dr.phil', 'dr.philos', 'drs', 'e.g', 'ens', 'esp', 'esq', 'etc', 'exp', 'expy', 'ext', 'feb', 'fed', 'fla', 'ft', 'fwy', 'fy', 'ga', 'gen', 'gov', 'hon', 'hosp', 'hr', 'hway', 'hwy', 'i.e', 'ia', 'id', 'ida', 'ill', 'inc', 'ind', 'ing', 'insp', 'is', 'jan', 'jr', 'jul', 'jun', 'kan', 'kans', 'ken', 'ky', 'la', 'lt', 'ltd', 'maj', 'man', 'mar', 'mass', 'may', 'md', 'me', 'med', 'messrs', 'mex', 'mfg', 'mich', 'min', 'minn', 'miss', 'mlle', 'mm', 'mme', 'mo', 'mont', 'mr', 'mrs', 'ms', 'msgr', 'mssrs', 'mt', 'mtn', 'neb', 'nebr', 'nev', 'no', 'nos', 'nov', 'nr', 'oct', 'ok', 'okla', 'ont', 'op', 'ord', 'ore', 'p', 'pa', 'pd', 'pde', 'penn', 'penna', 'pfc', 'ph', 'ph.d', 'pl', 'plz', 'pp', 'prof', 'pvt', 'que', 'rd', 'rs', 'ref', 'rep', 'reps', 'res', 'rev', 'rt', 'sask', 'sec', 'sen', 'sens', 'sep', 'sept', 'sfc', 'sgt', 'sr', 'st', 'supt', 'surg', 'tce', 'tenn', 'tex', 'univ', 'usafa', 'u.s', 'ut', 'va', 'v', 'ver', 'viz', 'vs', 'vt', 'wash', 'wis', 'wisc', 'wy', 'wyo', 'yuk', 'fig']
        PREPOSITIVE_ABBREVIATIONS = ['adm', 'attys', 'brig', 'capt', 'cmdr', 'col', 'cpl', 'det', 'dr', 'gen', 'gov', 'ing', 'lt', 'maj', 'mr', 'mrs', 'ms', 'mt', 'messrs', 'mssrs', 'prof', 'ph', 'rep', 'reps', 'rev', 'sen', 'sens', 'sgt', 'st', 'supt', 'v', 'vs', 'fig']
        NUMBER_ABBREVIATIONS = ['art', 'ext', 'no', 'nos', 'p', 'pp']

        # Part of "Abbreviations" ruby module
        # Rubular: http://rubular.com/r/EUbZCNfgei
        WithMultiplePeriodsAndEmailRule = Rule(r'(\w)(\.)(\w)', '\\1∮\\3')

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
