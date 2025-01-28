from random import randrange
import random
import match
import wrestlers
import matchClass
import json

with open('wrestlerRoster.json', 'r') as file:
    wrestler_data = json.load(file)

# Create Wrestler objects and store them in a dictionary
wrestledict = {
    key: wrestlers.Wrestler(
        name=value["name"],
        overall=value["overall"],
        height=value["height"],
        weight=value["weight"],
        music=value["music"],
        entrance=value["entrance"],
        catchphrase=value["catchphrase"],
        tauntstyle=value["tauntstyle"],
        hometown=value["hometown"],
        align=value["align"],
        mic_skill=value["mic_skill"],
        style=value["style"],
        signature=value["signature"],
        signaturetype=value["signaturetype"],
        finisher=value["finisher"],
        finishertype=value["finishertype"]
    )
    for key, value in wrestler_data.items()
}


print("Welcome to Main Event!")
winner, loser = random.sample(list(wrestledict.values()), 2)
oneonone = matchClass.Match(winner, loser, 20, False)
oneonone.load_data('matchStrings.json')
oneonone.matchDirector()



