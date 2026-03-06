text = """
U lavice dítě stálo z plna hrdla křičelo Bodejž jsi jen trochu málo ty
cikáně mlčelo

Poledne v tom okamžení táta přijde z roboty a mně hasne u vaření pro
tebe ty zlobo ty

Mlč Hle husar a kočárek hrej si tu máš kohouta Než kohout vůz i husárek
bouch bác letí do kouta

A zas do hrozného křiku I bodejž tě sršeň sám Že na tebe nezvedníku
Polednici zavolám

Pojď si proň ty Polednice pojď vem si ho zlostníka A hle tu kdos u
světnice dvéře zlehka odmyká

Malá hnědá tváři divé pod plachetkou osoba o berličce hnáty křivé hlas
vichřice podoba

Dej sem dítě Kriste Pane odpusť hříchy hříšnici Div že smrt ji neovane
ejhle tuť Polednici

Ke stolu se plíží tiše Polednice jako stín matka hrůzou sotva dýše dítě
chopíc na svůj klín

A vinouc je zpět pohlíží běda běda dítěti Polednice blíž se plíží blíž a
již je vzápětí

Již vztahuje po něm ruku matka tisknouc ramena Pro Kristovu drahou muku
klesá smyslů zbavena

Tu slyš jedna druhá třetí poledne zvon udeří klika cvakla dvéře letí
táta vchází do dveří

Ve mdlobách tu matka leží k ňadrům dítě přimknuté matku vzkřísil ještě
stěží avšak dítě zalknuté
"""

# Převedeme vše na malá písmena, aby se počítala i velká "A"
text_lower = text.lower()

# Spočítáme výskyty
pocet_a = text_lower.count('a')
pocet_a_cara = text_lower.count('á')

print(f"Počet písmen 'a': {pocet_a}")
print(f"Počet písmen 'á': {pocet_a_cara}")
print(f"Celkem 'a' + 'á': {pocet_a + pocet_a_cara}")
