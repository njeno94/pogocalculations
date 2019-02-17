#!/bin/python

import requests
import sys

r = requests.get("https://gamepress.gg/json-list?_format=json&game_tid=1")
jsonlinks = r.json()

for i in jsonlinks:
    if i["title"] == "attack-PoGO":
        attackurl = i["url"]
    if i["title"] == "defense-PoGO":
        defenseurl = i["url"]
    if i["title"] == "stamina-PoGO":
        staminaurl = i["url"]
attreq = requests.get(attackurl)
defreq = requests.get(defenseurl)
stareq = requests.get(staminaurl)

attjson = attreq.json()
defjson = defreq.json()
stajson = stareq.json()

separator = " "
name = separator.join(sys.argv[1:])

for i in attjson:
    if i["title"] == name:
        attack=i["field_base_attack"]
        break
for i in defjson:
    if i["title"] == name:
        defense=i["field_base_defense"]
        break
for i in stajson:
    if i["title"] == name:
        stamina=i["field_base_stamina"]
        break

print("{0},{1},{2}".format(attack,defense,stamina))
