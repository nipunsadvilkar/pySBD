import os

def addLang(lang_code,lang,delimiter = "['.', '!', '?']",testcase = ""):
    # making new file language.py
    f = open(os.path.join("pysbd","lang",lang+".py"),'w')
    lang_py = "from pysbd.abbreviation_replacer import AbbreviationReplacer\n\n"+"from pysbd.lang.common import Common, Standard\n\n"+"class "+lang.capitalize()+"(Common, Standard):\n"+"    SENTENCE_BOUNDARY_REGEX = r'.*?[.!?]|.*?$'\n"+  "    Punctuations = "+delimiter+"\n\n"+              "    class AbbreviationReplacer(AbbreviationReplacer):\n"+"        SENTENCE_STARTERS = []\n"
    f.write(lang_py)
    f.close()

    # appending language to conftest.py
    f = open(os.path.join("tests","conftest.py"),"a")
    conftest_py = "\n\n@pytest.fixture()\n"+"def "+lang_code+"_default_fixture():\n"+"    "+lang_code+"_segmenter = pysbd.Segmenter(language='"+lang_code+"', clean=False, char_span=False)\n"+"    return "+lang_code+"_segmenter\n"
    f.write(conftest_py)
    f.close()

    # making new file test_language.py
    f = open(os.path.join("tests","lang","test_"+lang+".py"),"w")
    test_lang_py = "import pytest\n\n"+"GOLDEN_"+lang_code.upper()+"_RULES_TEST_CASES = "+"["+testcase+"]\n\n"+"@pytest.mark.parametrize('text,expected_sents', GOLDEN_"+lang_code.upper()+"_RULES_TEST_CASES)\n"+"def test_"+lang_code+"_sbd("+lang_code+"_default_fixture, text, expected_sents):\n"+'    """'+lang+' language SBD tests"""\n'+"    segments = "+lang_code+"_default_fixture.segment(text)\n"+"    assert segments == expected_sents"
    f.write(test_lang_py)
    f.close()

    f_import = open(os.path.join("temp","import.txt"),"a")
    import_str = "\nfrom pysbd.lang."+lang+" import "+lang.capitalize()
    f_import.write(import_str)
    f_import.close()

    f_language_code = open(os.path.join("temp","language_code.txt"),"a")
    language_code_str = ",\n    '"+lang_code+"': "+lang.capitalize() 
    f_language_code.write(language_code_str)
    f_language_code.close()

    with open(os.path.join("temp","import.txt"),"r") as f_import:
        data_import = f_import.readlines() 
    f_import.close()

    with open(os.path.join("temp","language_code.txt"),"r") as f_language_code:
        data_language_code = f_language_code.readlines()
    f_language_code.close()

    languages_py = "# -*- coding: utf-8 -*-\n"
    
    for i in data_import:
        languages_py = languages_py+i
    
    languages_py = languages_py+"\n\nLANGUAGE_CODES = {\n"

    for i in data_language_code:
        languages_py = languages_py+i
    
    languages_py = languages_py+"\n}\n\n"+"class Language(object):\n\n"+"    def __init__(self, code):\n"+"        self.code = code\n\n"+"    @classmethod\n"+"    def get_language_code(cls, code):\n"+"        try:\n"+"            return LANGUAGE_CODES[code]\n"+"        except KeyError:\n"+'            raise ValueError("Provide valid language ID i.e. ISO code. "\n'+'                "Available codes are : {}".format(set(LANGUAGE_CODES.keys())))'

    f_languages_py = open(os.path.join("pysbd","languages.py"),'w')
    f_languages_py.write(languages_py)
    f_languages_py.close()


addLang("od","odia")
