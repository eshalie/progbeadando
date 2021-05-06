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



def eredmeny(csapatok):
    eredmenyek={}
    for i in range(0,len(csapatok)-1):
            for j in range(i+1,len(csapatok)):
                gol1 = str(random.randint(0,4))
                gol2= str(random.randint(0,4))
                eredmenyek[f'{csapatok[i]} {csapatok[j]}'] = f'{gol1}:{gol2}'
    return eredmenyek


def pontszamitas(eredmenyek):
    pontok=np.zeros(n)
    rugottgol=np.zeros(n)
    kapottgol=np.zeros(n)

    for i in range(len(csapatok)):
        for kulcs, ertek in eredmenyek.items():
            kulcs=kulcs.split()
            ertek=ertek.split(':')
            otthoni=kulcs[0]
            otthonigol=int(ertek[0])
            vendeg=kulcs[1]
            vendeggol=int(ertek[1])
            if kulcs[i]==otthoni:
                if otthonigol>vendeggol:
                    pontok[i]+=3
                elif otthonigol==vendeggol:
                    pontok[i]+=1
                rugottgol[i]+=otthonigol
                kapottgol[i]+=vendeggol
            elif csapatok[i]==vendeg:
                if otthonigol<vendeggol:
                    pontok[i]+=3
                elif otthonigol==vendeggol:
                    pontok[i]+=1
                rugottgol[i]+=vendeggol
                kapottgol[i]+=otthonigol
    return pontok, rugottgol, kapottgol


def allas(pontok,rugottgolok,kapottgolok,csapatok):
    for i in range(0,len(pontok)-1):
        for j in range(i+1,len(pontok)):
            if pontok[i] < pontok[j]:
                pontok[i], pontok[j] = pontok[j], pontok[i]
                rugottgolok[i], rugottgolok[j] = rugottgolok[j], rugottgolok[i]
                kapottgolok[i], kapottgolok[j] = kapottgolok[j], kapottgolok[i]
                csapatok[i], csapatok[j] = csapatok[j], csapatok[i]

            elif pontok[i] == pontok[j]:
                if rugottgolok[j] > rugottgolok[i]:
                    pontok[i], pontok[j] = pontok[j], pontok[i]
                    rugottgolok[i], rugottgolok[j] = rugottgolok[j], rugottgolok[i]
                    kapottgolok[i], kapottgolok[j] = kapottgolok[j], kapottgolok[i]
                    csapatok[i], csapatok[j] = csapatok[j], csapatok[i]
    print("Pontállás:")
    print("Helyezés Név Pont Rúgott gólok Kapott gólok",i,csapatok[i],rugottgolok[i],kapottgolok[i])



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

pontok, rugottgol , kapottgol=pontszamitas(eredmeny(csapatok))
allas(pontok,rugottgol,kapottgol,csapatok)