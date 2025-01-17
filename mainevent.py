from random import randrange
import random
import match
import wrestlers

wrestledict = {
    "under": wrestlers.Wrestler("The Undertaker", 88, 55, "Powerhouse", "Tombstone Piledriver", "Grapple"),
    "rock": wrestlers.Wrestler("The Rock", 87, 60, "All-Around", "Rock Bottom", "Standing"),
    "austin": wrestlers.Wrestler("Steve Austin", 92, 85, "Brawler", "Stone Cold Stunner", "Standing")
}

print("Wrestler Dictionary Contents:")
for key, wrestler in wrestledict.items():
    print(f"{key}: {wrestler}")

print("Welcome to Main Event!")
winner, loser = random.sample(list(wrestledict.values()), 2)
match.matchDirector(winner, loser, 20)
print("End")


