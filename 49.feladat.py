"""Készítsen egy programot amely megkapja egy termék összetevőit szövegként. A program
ismerje fel a legfontosabb allergéneket (https://csakamentes.hu/14-allergen-reszletesen/).
Mentse le ezen allergén anyagoknak az előfordulási számait (a szövegben hányszor
szerepelnek) és jelenítse meg könnyen áttekinthető formában, matplotlib segítségével (pl.
oszlopdiagram). Alakítsa ezek után úgy a programot, hogy annak file-ként meg lehet adni a
beolvasandó szöveget és ki lehet választani mely allergénekre vagyunk érzékenyek. Ezeket a
matplotlib ábrázoláson jelölje külön (pl. színezéssel) és mentse le egy kimeneti mappába az
elemzés eredményét"""

import numpy as np
import matplotlib.pyplot as plt

def szamlalo(file,allergen):
    tmp=len(allergen)
    szamlalo=np.zeros(tmp,dtype=int)
    for i in range(len(file)):
        for j in range(len(allergen)):
            if allergen[j] in file[i]:
                szamlalo[j]+=1
    return szamlalo

def sajatallergia(sall,allergenek,szaml):
    tmp = len(allergenek)
    sajatallergia = np.zeros(tmp, dtype=int)
    for i in range(len(sajatallergia)):
        for j in range(len(sall)):
            if szaml[i]!=0 and sall[j] in allergenek[i]:
                sajatallergia[i]=1
    return sajatallergia

try:
    ifile = open("input2.txt","r",encoding='utf-8')
    afile=open("allergen.txt","r",encoding='utf-8')
    allergenek=afile.read().lower().split(", ")
    osszetevok=ifile.read().lower().split(", ")
    sall=input("Kérem adja meg allergéneit vesszővel elválasztva: ")
    sall=sall.lower().split(",")
    szaml=szamlalo(osszetevok,allergenek)
    sallsz=sajatallergia(sall,allergenek,szaml)
    oszlopok=plt.bar(allergenek, szaml, color="Blue")
    plt.xticks(fontsize=10, rotation=45)
    plt.xlabel("Allergének")
    plt.ylabel("Előfordulás")
    for i in range(len(sallsz)):
        if sallsz[i]==1:
            oszlopok[i].set_color('r')
    plt.savefig("49/kutatas.png")
    plt.show()
    afile.close()
    ifile.close()
except FileNotFoundError:
    print("input2.txt or allergen.txt nem letezik")