import os
from time import sleep


def install():
    """
    installs the latest build on the local machine
    """
    print("Installing Local iteration of PySBD...")
    sleep(3)
    os.system('"python setup.py install"')
    print("Installed Local iteration of PySBD...")
    sleep(1)
    print("")
    sleep(1)


# uncomment to install the Local version of PySBD
# install()

import pysbd


def testHelper(text):
    """
    text: Single string of multiple sentences
    return: a list of individual sentences.
    """
    print("Running Test...")
    # text = "గుంటూరులో హైకోర్టు ఏర్పాటు చేసారు. ఈ భీకర కాల్పుల్లో నలుగురు ఉగ్రవాదులు హతమయ్యారు."
    seg = pysbd.Segmenter(language="te", clean=False)
    # print(seg.segment(text))
    return seg.segment(text)


def test(install_bool = False):
    if install_bool:
        install();

    file_list = os.listdir('input')
    for file in file_list:
        with open(os.path.join('input', file), 'r', encoding='utf8') as f1:
            contents = f1.read()
            # print(type(contents))
            lines = testHelper(contents)
            f2 = open(os.path.join('output', file[:-4:] + "_split.txt"), 'w', encoding='utf8')
            for line in lines:
                f2.write("%s\n" % line)


test(True)
