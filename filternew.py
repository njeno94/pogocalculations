#!/bin/python

import sys

cpm=(0.094,0.16639787,0.21573247,0.25572005,0.29024988,0.3210876,0.34921268,0.37523559,0.39956728,0.42250001,0.44310755,0.46279839,0.48168495,0.49985844,0.51739395,0.53435433,0.55079269,0.56675452,0.58227891,0.59740001,0.61215729,0.62656713,0.64065295,0.65443563,0.667934,0.68116492,0.69414365,0.70688421,0.71939909,0.7317,0.73776948,0.74378943,0.74976104,0.75568551,0.76156384,0.76739717,0.7731865,0.77893275,0.78463697,0.79030001)

baseattack=sys.argv[1]
basedefence=sys.argv[2]
basestamina=sys.argv[3]

#maxivmissing=sys.argv[4]
#minattackiv=sys.argv[5]
#mindefenceiv=sys.argv[6]
#minstaminaiv=sys.argv[7]

def calccp(a,d,s):
    return a*d**(1/2)*s**(1/2)/10

for c in cpm:
    attack=baseattack+15
    defence=basedefence+15
    stamina=basestamina+15
    print(calccp(attack,defence,stamina)

