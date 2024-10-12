
import time


print("Ahoj, já jsem jednoduchý kvíz :-)")
print("Tuto hru vytvořil NNW Developer")
print("Pravidla:")
print("Hra začíná výběrem A/N, pokud chcete hrát napište A pokud nechcete napište N, když napíšete N tak se Vám hra automaticky zavře.  Pokud dáte A, tak se Vám spustí kvíz. Vždy máte na výběr ze tří otázek, do pole pak napíšete pouze číslo dané otázky bez tečky. To znamená, že když budu chtít odpovědět odpovědí č.3, tak napíšu pouze číslo 3 atd. Při zadání špatné odpovědi Vám to hra sdělí a řekne, jak to má být správně. Pro opravu odpovědi, hru zavřete a spusťte znova. Užijte si hru :-)")

print("Jsi připravený?  A/N")
promnena1= input()
if promnena1.lower() == ("a"):print("Dobře, jdeme na to :-)")
if promnena1.lower() == ("n"):quit()

print("První otázka je: Kdo byl Václav Havel?")

print("1. ","Budoucí manžel od Shopaholic Adel")
print("2. ","1. prezident České Republiky")
print("3. ","2. syn od Andreje Babiše")

while True:
    x1 = input()
    if x1 not in {"1","2","3"}:print("Musíte zadat odpověď v intervalu 1-3")
    elif x1 == "2":
        print("Ano, správně. Druhá otázka: Kdy vznikla samostatná Československá republika?")
        break
    elif x1 == "1":
        print("Ne, špatně, správná odpověď je", "2.  1. prezident České Republiky!")
        break
    elif x1 == "3":
        print("Ne, špatně, správná odpověď je", "2.  1. prezident České Republiky!")
        break

print("Druhá otázka: Kdy vznikla samostatná Československá republika?")

print("1. ","1918")
print("2. ","1993")
print("3. ","1914")

while True:
    x2 = input()
    if x2 not in {"1","2","3"}:print("Musíte zadat odpověď v intervalu 1-3")
    elif x2 == "1":
        print("Ano správně!")
        break
    elif x2 == "2":
        print("Ne, špatně, správná odpověď je", "1. 1918!")
        break
    elif x2 == "3":
        print("Ne, špatně, správná odpověď je", "1. 1918!")
        break



print("Třetí otázka: Co to je Perl ?")

print("1. ","Mužská verze od mořské perly")
print("2. ","Označení hloupého velblouda")
print("3. ","Programovací jazyk")

while True:
    x3 = input()
    if x3 not in {"1","2","3"}:print("Musíte zadat odpověď v intervalu 1-3")
    elif x3 == "3":
        print("Ano správně!")
        break
    elif x3 == "2":
        print("Ne, špatně, správná odpověď je", "3. Programovací jazyk!")
        break
    elif x3 == "1":
        print("Ne, špatně, správná odpověď je", "3. Programovací jazyk!")
        break


print("Huráá! Dokončil jsi kvíz, pokud jsi byl spokojený, nebo tě napadají další otázky, které bych měl doplnit, tak mi napiš na https://nonamewebsite.neocities.org/formular.html")





time.sleep(15)


