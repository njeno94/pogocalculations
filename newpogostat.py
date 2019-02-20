#!/bin/python

import requests

r = requests.get("https://gamepress.gg/sites/default/files/aggregatedjson/pokemon-data-full-en-PoGO.json")

pokedex = r.json()

def getstatsbyname(name):
    for poke in pokedex:
        if poke["title_1"] == name:
            attack =  int(poke["atk"])
            defense = int(poke["def"])
            stamina = int(poke["sta"])
            dexid = poke["number"]
            break
    return { "name":name, "attack":attack, "defense":defense, "stamina":stamina, "dexid":dexid }
