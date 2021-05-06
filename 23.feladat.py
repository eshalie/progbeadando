"""Írjon programot, amely egy labdarúgó bajnokság meccseit képes legenerálni, és ez alapján
egy rangsort kialakítani a csapatok között. A program először kérjen be egy n számot, majd
pedig n darab csapat nevét. Ezt követően pedig random generálja le a csapatok egymás
elleni meccseinek eredményeit (mindenki játsszon mindenkivel elven), amit a pálda
kimenet alapján kiír a program. A program végül készítsen egy eredménytáblát a meccsek
eredményei alapján (lásd példa kimenet). Pontozás: győzelem: 3 pont, döntetlen: 1 pont,
vereség: 0pont. Ha két csapat azonos pontszámmal végez, akkor közöttük a gólkülönbség
(rúgott gólok – kapott gólok) rangsorol."""

import numpy as np
import random
import itertools


while True:
    n=input("Adjon meg egy számot:")
    if n.isnumeric():   #ellenőrizzük, hogy az input szám e
        n=int(n)
        if n<=1:    #Ellenőrizzük, hogy a megadott szám nagyobb e egynél, ugyanis egy csapat nem tud versenyezni
            print("Kérem legalább kettőt adjon meg")
        else:
            break
    else:
        print("Kérem számot adjon meg")

csapatok=[""]
csapatok[0]=input("Adjon meg egy csapat nevet ")
db=1

while True:
    tmp=input("Adjon meg egy csapat nevet ")
    if tmp in csapatok:     #Ellenőrizzük, hogy a csapatnév szerepel e már a listában
        print("Ez a csapat már a listában van kérem adjon meg másik csapat nevet")
    else:
        csapatok.append(tmp)
        db+=1
        if db==n:
            break

csapat_parok=list(itertools.combinations(csapatok, 2))      #megalkotjuk a csapatpárokat
print(csapatok,csapat_parok)
