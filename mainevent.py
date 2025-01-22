from random import randrange
import random
import match
import wrestlers
import matchClass

wrestledict = {
    "under": wrestlers.Wrestler("The Undertaker", 88, 55, "Powerhouse", "Tombstone Piledriver", "Grapple"),
    "rock": wrestlers.Wrestler("The Rock", 87, 60, "All-Around", "Rock Bottom", "Standing"),
    "austin": wrestlers.Wrestler("Steve Austin", 92, 85, "Brawler", "Stone Cold Stunner", "Standing"),
    "hbk": wrestlers.Wrestler("Shawn Michaels", 90, 40, "All-Around", "Sweet Chin Music", "Standing"),
    "brock": wrestlers.Wrestler("Brock Lesnar", 85, 53, "All-Around", "F5", "Grapple"),
    "jake": wrestlers.Wrestler("Jake Roberts", 78, 65, "Brawler", "DDT", "Standing")
}

print("Wrestler Dictionary Contents:")
for key, wrestler in wrestledict.items():
    print(f"{key}: {wrestler}")

print("Welcome to Main Event!")
winner, loser = random.sample(list(wrestledict.values()), 2)
oneonone = matchClass.Match(winner, loser, 20, False)
oneonone.matchDirector()
#match.matchDirector(winner, loser, 10, True)
print("End")


