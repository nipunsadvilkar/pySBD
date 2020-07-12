# -*- coding: utf-8 -*-
import pytest
import pysbd

GOLDEN_ES_RULES_TEST_CASES = [
    ("¿Cómo está hoy? Espero que muy bien.",
     ["¿Cómo está hoy?", "Espero que muy bien."]),
    ("¡Hola señorita! Espero que muy bien.",
     ["¡Hola señorita!", "Espero que muy bien."]),
    ("Hola Srta. Ledesma. Buenos días, soy el Lic. Naser Pastoriza, y él es mi padre, el Dr. Naser.",
     ["Hola Srta. Ledesma.", "Buenos días, soy el Lic. Naser Pastoriza, y él es mi padre, el Dr. Naser."]),
    ("¡La casa cuesta $170.500.000,00! ¡Muy costosa! Se prevé una disminución del 12.5% para el próximo año.",
     ["¡La casa cuesta $170.500.000,00!", "¡Muy costosa!", "Se prevé una disminución del 12.5% para el próximo año."]),
    ("«Ninguna mente extraordinaria está exenta de un toque de demencia.», dijo Aristóteles.",
     ["«Ninguna mente extraordinaria está exenta de un toque de demencia.», dijo Aristóteles."]
    )
]

ES_MORE_TEST_CASES = [
('«Ninguna mente extraordinaria está exenta de un toque de demencia», dijo Aristóteles. Pablo, ¿adónde vas? ¡¿Qué viste?!',
['«Ninguna mente extraordinaria está exenta de un toque de demencia», dijo Aristóteles.', 'Pablo, ¿adónde vas?', '¡¿Qué viste?!']),

('Admón. es administración o me equivoco.',
['Admón. es administración o me equivoco.']),

("¡Hola Srta. Ledesma! ¿Cómo está hoy? Espero que muy bien.",
["¡Hola Srta. Ledesma!",  "¿Cómo está hoy?", "Espero que muy bien."]),

("Buenos días, soy el Lic. Naser Pastoriza, y él es mi padre, el Dr. Naser.",
["Buenos días, soy el Lic. Naser Pastoriza, y él es mi padre, el Dr. Naser."]),

("He apuntado una cita para la siguiente fecha: Mar. 23 de Nov. de 2014. Gracias.",
["He apuntado una cita para la siguiente fecha: Mar. 23 de Nov. de 2014.", "Gracias."]),

("Núm. de tel: 351.123.465.4. Envíe mis saludos a la Sra. Rescia.",
["Núm. de tel: 351.123.465.4.", "Envíe mis saludos a la Sra. Rescia."]),

("Cero en la escala Celsius o de grados centígrados (0 °C) se define como el equivalente a 273.15 K, con una diferencia de temperatura de 1 °C equivalente a una diferencia de 1 Kelvin. Esto significa que 100 °C, definido como el punto de ebullición del agua, se define como el equivalente a 373.15 K.",
["Cero en la escala Celsius o de grados centígrados (0 °C) se define como el equivalente a 273.15 K, con una diferencia de temperatura de 1 °C equivalente a una diferencia de 1 Kelvin.", "Esto significa que 100 °C, definido como el punto de ebullición del agua, se define como el equivalente a 373.15 K."]),

("Durante la primera misión del Discovery (30 Ago. 1984 15:08.10) tuvo lugar el lanzamiento de dos satélites de comunicación, el nombre de esta misión fue STS-41-D.",
["Durante la primera misión del Discovery (30 Ago. 1984 15:08.10) tuvo lugar el lanzamiento de dos satélites de comunicación, el nombre de esta misión fue STS-41-D."]),


("Frase del gran José Hernández: \"Aquí me pongo a cantar / al compás de la vigüela, / que el hombre que lo desvela / una pena estrordinaria, / como la ave solitaria / con el cantar se consuela. / [...] \".",
["Frase del gran José Hernández: \"Aquí me pongo a cantar / al compás de la vigüela, / que el hombre que lo desvela / una pena estrordinaria, / como la ave solitaria / con el cantar se consuela. / [...] \"."]),

("Citando a Criss Jami «Prefiero ser un artista a ser un líder, irónicamente, un líder tiene que seguir las reglas.», lo cual parece muy acertado.",
["Citando a Criss Jami «Prefiero ser un artista a ser un líder, irónicamente, un líder tiene que seguir las reglas.», lo cual parece muy acertado."]),

("Cuando llegué, le estaba dando ejercicios a los niños, uno de los cuales era \"3 + (14/7).x = 5\". ¿Qué te parece?",
["Cuando llegué, le estaba dando ejercicios a los niños, uno de los cuales era \"3 + (14/7).x = 5\".", "¿Qué te parece?"]),

("Se le pidió a los niños que leyeran los párrf. 5 y 6 del art. 4 de la constitución de los EE. UU..",
["Se le pidió a los niños que leyeran los párrf. 5 y 6 del art. 4 de la constitución de los EE. UU.."]),

("Una de las preguntas realizadas en la evaluación del día Lun. 15 de Mar. fue la siguiente: \"Alumnos, ¿cuál es el resultado de la operación 1.1 + 4/5?\". Disponían de 1 min. para responder esa pregunta.",
["Una de las preguntas realizadas en la evaluación del día Lun. 15 de Mar. fue la siguiente: \"Alumnos, ¿cuál es el resultado de la operación 1.1 + 4/5?\".", "Disponían de 1 min. para responder esa pregunta."]),
("La temperatura del motor alcanzó los 120.5°C. Afortunadamente, pudo llegar al final de carrera.",
["La temperatura del motor alcanzó los 120.5°C.", "Afortunadamente, pudo llegar al final de carrera."]),
("El volumen del cuerpo es 3m³. ¿Cuál es la superficie de cada cara del prisma?",
["El volumen del cuerpo es 3m³.", "¿Cuál es la superficie de cada cara del prisma?"]),
("La habitación tiene 20.55m². El living tiene 50.0m².",
["La habitación tiene 20.55m².", "El living tiene 50.0m²."]),
("1°C corresponde a 33.8°F. ¿A cuánto corresponde 35°C?",
["1°C corresponde a 33.8°F.", "¿A cuánto corresponde 35°C?"]),
("Hamilton ganó el último gran premio de Fórmula 1, luego de 1:39:02.619 Hs. de carrera, segundo resultó Massa, a una diferencia de 2.5 segundos. De esta manera se consagró ¡Campeón mundial!",
["Hamilton ganó el último gran premio de Fórmula 1, luego de 1:39:02.619 Hs. de carrera, segundo resultó Massa, a una diferencia de 2.5 segundos.", "De esta manera se consagró ¡Campeón mundial!"]),
("¡La casa cuesta $170.500.000,00! ¡Muy costosa! Se prevé una disminución del 12.5% para el próximo año.",
["¡La casa cuesta $170.500.000,00!", "¡Muy costosa!", "Se prevé una disminución del 12.5% para el próximo año."]),
("El corredor No. 103 arrivó 4°.",
["El corredor No. 103 arrivó 4°."]),
("Hoy es 27/04/2014, y es mi cumpleaños. ¿Cuándo es el tuyo?",
["Hoy es 27/04/2014, y es mi cumpleaños.", "¿Cuándo es el tuyo?"]),
("Aquí está la lista de compras para el almuerzo: 1.Helado, 2.Carne, 3.Arroz. ¿Cuánto costará? Quizás $12.5.",
["Aquí está la lista de compras para el almuerzo: 1.Helado, 2.Carne, 3.Arroz.", "¿Cuánto costará?", "Quizás $12.5."]),
("1 + 1 es 2. 2 + 2 es 4. El auto es de color rojo.",
["1 + 1 es 2.", "2 + 2 es 4.", "El auto es de color rojo."]),
("La máquina viajaba a 100 km/h. ¿En cuánto tiempo recorrió los 153 Km.?",
["La máquina viajaba a 100 km/h.", "¿En cuánto tiempo recorrió los 153 Km.?"]),
("Explora oportunidades de carrera en el área de Salud en el Hospital de Northern en Mt. Kisco.",
["Explora oportunidades de carrera en el área de Salud en el Hospital de Northern en Mt. Kisco."])
]

ES_CLEAN_TEST_CASES = [("\n \nCentro de Relaciones Interinstitucionales -CERI \n\nCra. 7 No. 40-53 Piso 10 Tel.  (57-1) 3239300 Ext. 1010 Fax: (57-1) 3402973 Bogotá, D.C. - Colombia \n\nhttp://www.udistrital.edu.co - http://ceri.udistrital.edu.co - relinter@udistrital.edu.co \n\n \n\nCERI 0908 \n \nBogotá, D.C. 6 de noviembre de 2014.  \n \nSeñores: \nEMBAJADA DE UNITED KINGDOM \n \n",
["Centro de Relaciones Interinstitucionales -CERI", "Cra. 7 No. 40-53 Piso 10 Tel.  (57-1) 3239300 Ext. 1010 Fax: (57-1) 3402973 Bogotá, D.C. - Colombia", "http://www.udistrital.edu.co - http://ceri.udistrital.edu.co - relinter@udistrital.edu.co", "CERI 0908", "Bogotá, D.C. 6 de noviembre de 2014.", "Señores:", "EMBAJADA DE UNITED KINGDOM"]),
("N°. 1026.253.553",
["N°. 1026.253.553"]),
("\n__________________________________________________________\nEl Board para Servicios Educativos de Putnam/Northern Westchester según el título IX, Sección 504 del “Rehabilitation Act” del 1973, del Título VII y del Acta “American with Disabilities” no discrimina para la admisión a programas educativos por sexo, creencia, nacionalidad, origen, edad o discapacidad.",
["__________________________________________________________", "El Board para Servicios Educativos de Putnam/Northern Westchester según el título IX, Sección 504 del “Rehabilitation Act” del 1973, del Título VII y del Acta “American with Disabilities” no discrimina para la admisión a programas educativos por sexo, creencia, nacionalidad, origen, edad o discapacidad."]),
("• 1. Busca atención prenatal desde el principio \n• 2. Aliméntate bien \n• 3. Presta mucha atención a la higiene de los alimentos \n• 4. Toma suplementos de ácido fólico y come pescado \n• 5. Haz ejercicio regularmente \n• 6. Comienza a hacer ejercicios de Kegel \n• 7. Restringe el consumo de alcohol \n• 8. Disminuye el consumo de cafeína \n• 9. Deja de fumar \n• 10. Descansa",
["• 1. Busca atención prenatal desde el principio", "• 2. Aliméntate bien", "• 3. Presta mucha atención a la higiene de los alimentos", "• 4. Toma suplementos de ácido fólico y come pescado", "• 5. Haz ejercicio regularmente", "• 6. Comienza a hacer ejercicios de Kegel", "• 7. Restringe el consumo de alcohol", "• 8. Disminuye el consumo de cafeína", "• 9. Deja de fumar", "• 10. Descansa"]),
("• 1. Busca atención prenatal desde el principio \n• 2. Aliméntate bien \n• 3. Presta mucha atención a la higiene de los alimentos \n• 4. Toma suplementos de ácido fólico y come pescado \n• 5. Haz ejercicio regularmente \n• 6. Comienza a hacer ejercicios de Kegel \n• 7. Restringe el consumo de alcohol \n• 8. Disminuye el consumo de cafeína \n• 9. Deja de fumar \n• 10. Descansa \n• 11. Hola",
["• 1. Busca atención prenatal desde el principio", "• 2. Aliméntate bien", "• 3. Presta mucha atención a la higiene de los alimentos", "• 4. Toma suplementos de ácido fólico y come pescado", "• 5. Haz ejercicio regularmente", "• 6. Comienza a hacer ejercicios de Kegel", "• 7. Restringe el consumo de alcohol", "• 8. Disminuye el consumo de cafeína", "• 9. Deja de fumar", "• 10. Descansa", "• 11. Hola"])
]

@pytest.mark.parametrize('text,expected_sents', GOLDEN_ES_RULES_TEST_CASES)
def test_es_sbd(es_default_fixture, text, expected_sents):
    """Spanish (Espanol) language SBD tests from Pragmatic Segmenter"""
    segments = es_default_fixture.segment(text)
    segments = [s.strip() for s in segments]
    assert segments == expected_sents

@pytest.mark.parametrize('text,expected_sents', ES_MORE_TEST_CASES)
def test_es_sbd_more_examples(es_default_fixture, text, expected_sents):
    """Spanish (Espanol) language SBD tests from Pragmatic Segmenter Contributors"""
    segments = es_default_fixture.segment(text)
    segments = [s.strip() for s in segments]
    assert segments == expected_sents

@pytest.mark.parametrize('text,expected_sents', ES_CLEAN_TEST_CASES)
def test_es_sbd_more_examples(es_with_clean_no_span_fixture, text, expected_sents):
    """Spanish (Espanol) language SBD tests from Pragmatic Segmenter Contributors"""
    segments = es_with_clean_no_span_fixture.segment(text)
    segments = [s.strip() for s in segments]
    assert segments == expected_sents

ES_PDF_CASE = [("\nA continuación me permito presentar a la Ingeniera LAURA MILENA LEÓN \nSANDOVAL, identificada con el documento N°. 1026.253.553 de Bogotá, \negresada del Programa Ingeniería Industrial en el año 2012, quien se desatacó por \nsu excelencia académica, actualmente cursa el programa de Maestría en \nIngeniería Industrial y se encuentra en un intercambio cultural en Bangalore – \nIndia.",
["A continuación me permito presentar a la Ingeniera LAURA MILENA LEÓN SANDOVAL, identificada con el documento N°. 1026.253.553 de Bogotá, egresada del Programa Ingeniería Industrial en el año 2012, quien se desatacó por su excelencia académica, actualmente cursa el programa de Maestría en Ingeniería Industrial y se encuentra en un intercambio cultural en Bangalore – India."])]

@pytest.mark.parametrize('text,expected_sents', ES_PDF_CASE)
def test_es_pdf_type(text, expected_sents):
    """Spanish SBD tests from Pragmatic Segmenter for doctype:pdf"""
    seg = pysbd.Segmenter(language="es", clean=True, doc_type='pdf')
    segments = seg.segment(text)
    segments = [s.strip() for s in segments]
    assert segments == expected_sents
