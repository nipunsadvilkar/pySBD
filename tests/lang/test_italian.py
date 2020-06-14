# -*- coding: utf-8 -*-
import pytest

GOLDEN_IT_RULES_TEST_CASES = [
("Salve Sig.ra Mengoni! Come sta oggi?",
 ["Salve Sig.ra Mengoni!", "Come sta oggi?"]),
("Una lettera si può iniziare in questo modo «Il/la sottoscritto/a.».",
 ["Una lettera si può iniziare in questo modo «Il/la sottoscritto/a.»."]),
("La casa costa 170.500.000,00€!",
 ["La casa costa 170.500.000,00€!"])
]

IT_MORE_TEST_CASES = [
("Salve Sig.ra Mengoni! Come sta oggi?",
 ["Salve Sig.ra Mengoni!", "Come sta oggi?"]),
("Buongiorno! Sono l'Ing. Mengozzi. È presente l'Avv. Cassioni?",
 ["Buongiorno!", "Sono l'Ing. Mengozzi.", "È presente l'Avv. Cassioni?"]),
("Mi fissi un appuntamento per mar. 23 Nov.. Grazie.",
 ["Mi fissi un appuntamento per mar. 23 Nov..", "Grazie."]),
("Ecco il mio tel.:01234567. Mi saluti la Sig.na Manelli. Arrivederci.",
 ["Ecco il mio tel.:01234567.", "Mi saluti la Sig.na Manelli.", "Arrivederci."]),
("La centrale meteor. si è guastata. Gli idraul. son dovuti andare a sistemarla.",
 ["La centrale meteor. si è guastata.", "Gli idraul. son dovuti andare a sistemarla."]),
("Hanno creato un algoritmo allo st. d. arte. Si ringrazia lo psicol. Serenti.",
 ["Hanno creato un algoritmo allo st. d. arte.", "Si ringrazia lo psicol. Serenti."]),
("Chiamate il V.Cte. delle F.P., adesso!",
 ["Chiamate il V.Cte. delle F.P., adesso!"]),
("Giancarlo ha sostenuto l'esame di econ. az..",
 ["Giancarlo ha sostenuto l'esame di econ. az.."]),
("Stava viaggiando a 90 km/h verso la provincia di TR quando il Dott. Mesini ha sentito un rumore e si fermò!",
 ["Stava viaggiando a 90 km/h verso la provincia di TR quando il Dott. Mesini ha sentito un rumore e si fermò!"]),
("Egregio Dir. Amm., le faccio sapere che l'ascensore non funziona.",
 ["Egregio Dir. Amm., le faccio sapere che l'ascensore non funziona."]),
("Stava mangiando e/o dormendo.",
 ["Stava mangiando e/o dormendo."]),
("Ricordatevi che dom 25 Set. sarà il compleanno di Maria; dovremo darle un regalo.",
 ["Ricordatevi che dom 25 Set. sarà il compleanno di Maria; dovremo darle un regalo."]),
("La politica è quella della austerità; quindi verranno fatti tagli agli sprechi.",
 ["La politica è quella della austerità; quindi verranno fatti tagli agli sprechi."]),
("Nel tribunale, l'Avv. Fabrizi ha urlato \"Io, l'illustrissimo Fabrizi, vi si oppone!\".",
 ["Nel tribunale, l'Avv. Fabrizi ha urlato \"Io, l'illustrissimo Fabrizi, vi si oppone!\"."]),
("Le parti fisiche di un computer (ad es. RAM, CPU, tastiera, mouse, etc.) sono definiti HW.",
 ["Le parti fisiche di un computer (ad es. RAM, CPU, tastiera, mouse, etc.) sono definiti HW."]),
("La parola 'casa' è sinonimo di abitazione.",
 ["La parola 'casa' è sinonimo di abitazione."]),
("La \"Mulino Bianco\" fa alimentari pre-confezionati.",
 ["La \"Mulino Bianco\" fa alimentari pre-confezionati."]),
("\"Ei fu. Siccome immobile / dato il mortal sospiro / stette la spoglia immemore / orba di tanto spiro / [...]\" (Manzoni).",
 ["\"Ei fu. Siccome immobile / dato il mortal sospiro / stette la spoglia immemore / orba di tanto spiro / [...]\" (Manzoni)."]),
("Una lettera si può iniziare in questo modo «Il/la sottoscritto/a ... nato/a a ...».",
 ["Una lettera si può iniziare in questo modo «Il/la sottoscritto/a ... nato/a a ...»."]),
("Per casa, in uno degli esercizi per i bambini c'era \"3 + (14/7) = 5\"",
 ["Per casa, in uno degli esercizi per i bambini c'era \"3 + (14/7) = 5\""]),
("Ai bambini è stato chiesto di fare \"4:2*2\"",
 ["Ai bambini è stato chiesto di fare \"4:2*2\""]),
("La maestra esclamò: \"Bambini, quanto fa '2/3 + 4/3?'\".",
 ["La maestra esclamò: \"Bambini, quanto fa \'2/3 + 4/3?\'\"."]),
("Il motore misurava 120°C.",
 ["Il motore misurava 120°C."]),
("Il volume era di 3m³.",
 ["Il volume era di 3m³."]),
("La stanza misurava 20m².",
 ["La stanza misurava 20m²."]),
("1°C corrisponde a 33.8°F.",
 ["1°C corrisponde a 33.8°F."]),
("Oggi è il 27-10-14.",
 ["Oggi è il 27-10-14."]),
("La casa costa 170.500.000,00€!",
 ["La casa costa 170.500.000,00€!"]),
("Il corridore 103 è arrivato 4°.",
 ["Il corridore 103 è arrivato 4°."]),
("Oggi è il 27/10/2014.",
 ["Oggi è il 27/10/2014."]),
("Ecco l'elenco: 1.gelato, 2.carne, 3.riso.",
 ["Ecco l'elenco: 1.gelato, 2.carne, 3.riso."]),
("Devi comprare : 1)pesce 2)sale.",
 ["Devi comprare : 1)pesce 2)sale."]),
("La macchina viaggiava a 100 km/h.",
 ["La macchina viaggiava a 100 km/h."])
]

@pytest.mark.parametrize('text,expected_sents', GOLDEN_IT_RULES_TEST_CASES)
def test_it_sbd(it_default_fixture, text, expected_sents):
    """Italian language SBD tests"""
    segments = it_default_fixture.segment(text)
    assert segments == expected_sents

@pytest.mark.parametrize('text,expected_sents', IT_MORE_TEST_CASES)
def test_it_sbd_more_cases(it_default_fixture, text, expected_sents):
    """Italian language SBD tests more examples"""
    segments = it_default_fixture.segment(text)
    assert segments == expected_sents
