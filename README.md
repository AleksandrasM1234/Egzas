## Egzas

Projekto tikslas

Sukurti interaktyvią, naršyklėje veikiančią programą, kuri:

Leidžia natūralia lietuvių kalba užduoti klausimus apie 2024 m. mišrių komunalinių atliekų sudėtį Lietuvoje (pagal regionus ir vidurkius).
Automatiškai aptinka neįprastus (anomalius) atliekų procentus skirtingose savivaldybėse ir regionuose.
Padeda savivaldybių specialistams, atliekų tvarkytojams ir aplinkosaugininkams greičiau suprasti realią situaciją, aptikti galimas duomenų klaidas ar netikėtus pokyčius atliekų srautuose.

Programa naudoja modernius NLP metodus (semantinę paiešką su Sentence Transformers) ir mašininį mokymąsi (Isolation Forest anomalijų aptikimui) – tai tarpinio lygio AI prototipas, sprendžiantis realią Lietuvos atliekų valdymo problemą.

Kas yra BSA?

BSA = biologiškai skaidžios atliekos (komunalinės biologiškai skaidžios atliekos).
Tai atliekų grupė, kuri natūraliai suyra biologiniais procesais (pvz., kompostuojant ar sąvartyne). Lietuvoje BSA sudaro didelę mišrių komunalinių atliekų dalį ir yra labai svarbi siekiant ES tikslų mažinti šiltnamio efektą sukeliančių dujų emisijas iš sąvartynų.
Pagrindinės BSA rūšys tyrime:

Žaliosios atliekos (šakos, žolė, lapai)
Biologiškai skaidžios maisto ir virtuvės atliekos
Popierius/kartonas (biologiškai skaidus)
Mediena
Tekstilė (natūrali)
Kitos biologiškai skaidžios komunalinės atliekos

Lietuvoje siekiama, kad iki 2035 m. į sąvartynus patektų ne daugiau kaip 10 % BSA (dabar vidutiniškai ~40–60 % priklausomai nuo regiono).

Kas yra anomalijos šioje programoje?

Anomalija – tai neįprastai aukštas arba žemas atliekų procentas konkrečioje savivaldybėje/sezone, palyginti su kitais duomenimis.
Programa naudoja Isolation Forest algoritmą (unsupervised anomalijų aptikimo metodą), kuris:

Mokosi iš visų procentų (pavasaris, vasara, ruduo, žiema, bendras)
Pažymi ~10 % duomenų kaip „įtartinus“ (outliers)

Pavyzdžiai realybėje:

Vienoje savivaldybėje plastiko atliekų 35 % (kai vidurkis ~13–15 %)
Žaliųjų atliekų procentas žiemą staiga 0 %, o vasarą 40 %
Labai didelis inertinių atliekų (statybinių šiukšlių) kiekis mažoje savivaldybėje

Tokios anomalijos gali reikšti:

Duomenų klaidą / neteisingą matavimą
Sezoninį ar vietinį ypatumą (pvz., statybos bumas)
Blogą rūšiavimą ar netinkamą atliekų kaupimą

#Pagrindinės išvados iš projekto ir duomenų (2024 m.)

Didžiausia problema Lietuvoje lieka BSA
Vidutiniškai ~41–75 % mišrių komunalinių atliekų yra biologiškai skaidžios – tai reiškia, kad didelė dalis vis dar patenka į sąvartynus ir gamina metaną.
Dideli skirtumai tarp regionų
Klaipėdos ir Šiaulių regionuose BSA dalis dažnai >60 %
Vilniaus regione daugiau plastiko ir „kitų nepavojingų“ atliekų
Kai kuriuose regionuose (pvz., Panevėžio) maisto atliekos sudaro net 40 %+ – tai rodo potencialą atskiram maisto atliekų rūšiavimui

Anomalijos padeda greitai rasti „karštuosius taškus“
Programa aptinka savivaldybes, kuriose procentai stipriai nukrypsta (pvz., labai daug tekstilės, inertinių ar kitų atliekų) – tai ta vieta, kur verta pradėti tikrinti realybę vietoje.
