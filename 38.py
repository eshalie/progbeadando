"""Készítsen programot amely az input.txt-ből számhármasokat olvas be (k, l, m), ahol k egy
l-es számrendszerben megadott szám amit m-es számrendszerbe vált át. Végül az
output.txt-be írja az átváltott értékeket a 10 számrendszerbeli értékükkel együtt."""

import numpy as np

def atvaltas(klm):
    tmp=klm.split(', ')
    k=int(tmp[0])
    l=int(tmp[1])
    m=int(tmp[2])
    tizes = 0
    if l <= 10:
        szamjegyek = [int(i) for i in str(k)] #végigmegy a számon majd minden jegyet átvált int-é
    else:
        szamjegyek = [int(i, l) for i in str(k)] #ha esetleg nagyobb a számrendszer mint 10 és betű van akkor átváltja a számjegyet tizesbe
    szamjegyek = szamjegyek[::-1] #megfordítjuk a sorrendjét a számjegyeknek
    for i in range(len(szamjegyek)):
        tizes += szamjegyek[i] * l ** i
    atvaltott=np.base_repr(tizes,base=m)
    return atvaltott, tizes


try:
    ifile = open("input.txt","r")
    ofile = open("output.txt", "w")
    sorok=ifile.readlines()
    for i in sorok:
        tmp1,tmp2=atvaltas(i)
        tmp1=str(tmp1)
        tmp2=str(tmp2)
        ofile.write(tmp1)
        ofile.write(", ")
        ofile.write(tmp2)
        ofile.write("\n")
    ifile.close()
    ofile.close()
except FileNotFoundError:
    print("input.txt is not exists")
