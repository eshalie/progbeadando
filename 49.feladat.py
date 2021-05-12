"""Készítsen egy programot amely megkapja egy termék összetevőit szövegként. A program
ismerje fel a legfontosabb allergéneket (https://csakamentes.hu/14-allergen-reszletesen/).
Mentse le ezen allergén anyagoknak az előfordulási számait (a szövegben hányszor
szerepelnek) és jelenítse meg könnyen áttekinthető formában, matplotlib segítségével (pl.
oszlopdiagram). Alakítsa ezek után úgy a programot, hogy annak file-ként meg lehet adni a
beolvasandó szöveget és ki lehet választani mely allergénekre vagyunk érzékenyek. Ezeket a
matplotlib ábrázoláson jelölje külön (pl. színezéssel) és mentse le egy kimeneti mappába az
elemzés eredményét"""

import numpy as np

def szamlalo(file,allergen):
    tmp=len(allergen)
    szamlalo=np.zeros(tmp,dtype=int)
    for i in range(len(file)):
        for j in range(len(allergen)):
            if allergen[j] in file[i]:
                szamlalo[j]+=1
    return szamlalo

try:
    ifile = open("input2.txt","r")
    afile=open("allergen.txt","r")
    allergenek=afile.read().lower().split(", ")
    osszetevok=ifile.read().lower().split(", ")
    szaml=szamlalo(osszetevok,allergenek)
    print(allergenek)
    print(szaml)
    afile.close()
    ifile.close()
except FileNotFoundError:
    print("input2.txt or allergen.txt nem letezik")