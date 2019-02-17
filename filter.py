#!/bin/python

import sys
import math
import pogostat

allcpm=(0.094,0.16639787,0.21573247,0.25572005,0.29024988,0.3210876,0.34921268,0.37523559,0.39956728,0.42250001,0.44310755,0.46279839,0.48168495,0.49985844,0.51739395,0.53435433,0.55079269,0.56675452,0.58227891,0.59740001,0.61215729,0.62656713,0.64065295,0.65443563,0.667934,0.68116492,0.69414365,0.70688421,0.71939909,0.7317,0.73776948,0.74378943,0.74976104,0.75568551,0.76156384)



def calccp(attack,defense,stamina,cpmult):
    return max(10,math.floor(attack*defense**(1/2)*stamina**(1/2)*cpmult**2/10))

def calcstamina(stamina,cpmult):
    return max(10, math.floor(stamina*cpmult))

def cpstring(cp):
    return "cp"+str(cp)

def hpstring(hp):
    return "hp"+str(hp)

pokestats=pogostat.getstatsbyname()


baseattack=pokestats["attack"]
basedefence=pokestats["defense"]
basestamina=pokestats["stamina"]
name=pokestats["name"]


minattackiv=int(input())
mindefenceiv=int(input())
minstaminaiv=int(input())
maxivmissing=int(input())

cphp={}
for cpm in allcpm:
    for attackiv in range(minattackiv,16):
        attack=(baseattack+attackiv)
        if 15-attackiv<=maxivmissing:
            for defenceiv in range(mindefenceiv,16):
                defence=(basedefence+defenceiv)
                if 30-attackiv-defenceiv <= maxivmissing:
                    for staminaiv in range(minstaminaiv,16):
                        stamina=(basestamina+staminaiv)
                        if 45-attackiv-defenceiv-staminaiv <= maxivmissing:
                            cp=calccp(attack,defence,stamina,cpm)
                            hp=calcstamina(stamina,cpm)
                            if cp not in cphp:
                                cphp[cp]=set()
                            cphp[cp].add(hp)
print(name,end="&")
for cp in cphp:
    print("!"+cpstring(cp)+","+",".join(map(hpstring,cphp[cp])),end="&")
allcp=list(cphp.keys())
#for cp in allcp[:-1]:
#print("cp{0}".format(cp),end=",")
#print(allcp[-1])
print(",".join(map(cpstring,allcp)))
