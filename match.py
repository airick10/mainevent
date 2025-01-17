from random import randrange
import random
import wrestlers
import time

def matchDirector(winner, loser, matchTime):
    matchCounter = 1
    edge = "winner"
    while matchTime > matchCounter:
        if matchCounter == 1:
            edge = startMatch(winner, loser, edge)
            print(edge)
            time.sleep(1)
        else:
            edge = midMatch(winner, loser, edge)
            time.sleep(1)
        matchCounter += 1
    endMatch(winner,loser,edge)


def startMatch(winner, loser, edge):
    start = random.randrange(100)
    if start < 20:
        print(f"{loser.name} starts out on fire rushing {winner.name} with a flurry of punches!")
        return "loser"
    elif start < 60:
        print(f"Both fighters stare at each other. Slowly walking towards the center and gauge each other.")
        return "winner"
    else:
        print(f"{winner.name} dodges a punch and whips {loser.name} to the corner. He follows and starts to deliver a series of punches to {loser.name}!")
        return "winner"


def midMatch(winner, loser, edge):
    if random.randrange(100) < 30:
        edge = reversal(winner, loser, edge)
        time.sleep(1)
        if random.randrange(100) < 15:
            edge = suddenFinisher(winner, loser, edge)
            time.sleep(1)
    match_moves = {
        "loser": {
            "Powerhouse": [
                f"{loser.name} whips {winner.name} along the ropes!  Thunderous Powerslam!",
                f"{loser.name} picks {winner.name} up quickly and slams him to the ground like a rag doll! ",
                f"Look at this!  {loser.name} is licking his chops.  He picks up {winner.name} with both hands and delivers a double choke slam!",
                f"{loser.name} charges at {winner.name}, flattening him with a running shoulder block!",
                f"{loser.name} hoists {winner.name} onto his shoulder and plants him with a devastating powerslam!",
                f"{loser.name} catches {winner.name} mid-air and slams him down with a spine-crunching backbreaker!",
                f"{loser.name} grabs {winner.name} by the arm and yanks him into a thunderous short-arm clothesline!"
            ],
            "All-Around": [
                f"{loser.name} kicks him in the gut...  DDT!  {winner.name} drops to the mat!",
                f"After a knee to the gut, {loser.name} slips around... runs up and drops a bulldog!",
                f"{loser.name} flings {winner.name} to the ropes.  {loser.name} catches him in a fallaway slam!",
                f"{loser.name} surprises {winner.name} with a snap suplex! Smooth execution!",
                f"{loser.name} counters {winner.name}'s attack with a quick drop toe hold and transitions into a headlock!",
                f"{loser.name} springboards off the ropes and catches {winner.name} with a crossbody!",
                f"{loser.name} flips over {winner.name} in a sunset flip attempt! The ref slides in for a two-count!"
            ],
            "Brawler": [
                f"{loser.name} finishes a few punches with a dynamite clothesline!  Wow, what force!",
                f"{loser.name} throws {winner.name} to the ropes and connects with an elbow knocking {winner.name} down hard!",
                f"{loser.name} fires a punch!  And another!  Brings {winner.name} to his knees!  {loser.name} drops down a double ax handle!",
                f"{loser.name} unleashes a flurry of rights and lefts, driving {winner.name} back into the corner!",
                f"{loser.name} grabs {winner.name}'s head and repeatedly rams it into the turnbuckle!",
                f"{loser.name} levels {winner.name} with a stiff knee to the midsection, followed by a running boot!",
                f"{loser.name} hooks {winner.name}'s head and lands a rough neckbreaker!"
            ]
        },
        "winner": {
            "Powerhouse": [
                f"{winner.name} whips {loser.name} along the ropes!  Thunderous Powerslam!",
                f"{winner.name} picks {loser.name} up quickly and slams him to the ground like a rag doll! ",
                f"Look at this!  {winner.name} is licking his chops.  He picks up {loser.name} with both hands and delivers a double choke slam!",
                f"{winner.name} grabs {loser.name} in a bearhug and squeezes the life out of him!",
                f"{winner.name} scoops up {loser.name} and slams him down with an earth-shaking body slam!",
                f"{winner.name} picks {loser.name} up like a feather and hits a massive powerbomb!",
                f"{winner.name} lifts {loser.name} in a military press, holding him high before slamming him to the mat!"
            ],
            "All-Around": [
                f"{winner.name} kicks him in the gut...  DDT!  {winner.name} drops to the mat!",
                f"After a knee to the gut, {winner.name} slips around... runs up and drops a bulldog!",
                f"{winner.name} flings {winner.name} to the ropes.  {winner.name} catches him in a fallaway slam!",
                f"{winner.name} ducks under a clothesline and counters with a perfect German suplex!",
                f"{winner.name} climbs to the top rope and nails {loser.name} with a flying elbow drop!",
                f"{winner.name} grabs {loser.name}'s arm and pulls him into a picture-perfect arm drag!",
                f"{winner.name} counters {loser.name}'s move with a sharp enzuigiri to the back of the head!"
            ],
            "Brawler": [
                f"{winner.name} finishes a few punches with a dynamite clothesline!  Wow, what force!",
                f"{winner.name} throws {loser.name} to the ropes and connects with an elbow knocking {loser.name} down hard!",
                f"{winner.name} fires a punch!  And another!  Brings {loser.name} to his knees!  {winner.name} drops down a double ax handle!",
                f"{winner.name} pounds on {loser.name} with a relentless series of punches, driving him to the ground!",
                f"{winner.name} connects with a brutal headbutt, sending {loser.name} staggering!",
                f"{winner.name} traps {loser.name} in the corner and unloads with machine-gun-like punches!",
                f"{winner.name} catches {loser.name}'s kick and drops him with a dragon screw leg whip!"
            ]
        }
    }

    match_list = match_moves[edge][loser.style if edge == "loser" else winner.style]

    print(random.choice(match_list))
    return edge

def reversal(winner, loser, edge):
    loserreversals = [
        f"Oh! What a reversal by {loser.name}!",
        f"{winner.name} tries to deliver a crushing blow, but {loser.name} reverses it beautifully!",
        f"{loser.name} counters with a stunning suplex on {winner.name}!",
        f"{loser.name} ducks under a clothesline and delivers a dropkick to {winner.name}!",
        f"{loser.name} reverses a grapple and sends {winner.name} crashing to the mat with a back body drop!",
        f"The crowd roars as {loser.name} counters with a jaw-dropping reversal!",
        f"{loser.name} sidesteps and slams {winner.name} into the turnbuckle!",
        f"{loser.name} catches {winner.name}'s arm and locks in a quick armbar before letting go!"
    ]
    winnerreversals = [
        f"Oh! What a reversal by {winner.name}!",
        f"{loser.name} tries to deliver a crushing blow, but {winner.name} reverses it beautifully!",
        f"{winner.name} counters with a stunning suplex on {loser.name}!",
        f"{winner.name} ducks under a clothesline and delivers a dropkick to {loser.name}!",
        f"{winner.name} reverses a grapple and sends {loser.name} crashing to the mat with a back body drop!",
        f"The crowd roars as {winner.name} counters with a jaw-dropping reversal!",
        f"{winner.name} sidesteps and slams {loser.name} into the turnbuckle!",
        f"{winner.name} catches {loser.name}'s arm and locks in a quick armbar before letting go!"
    ]

    if edge == "loser":
        print(random.choice(winnerreversals))
        return "winner"
    else:
        print(random.choice(loserreversals))
        return "loser"


def suddenFinisher(winner, loser, edge):
    finisher_scenarios = {
        "loser": {
            "Standing": [
                f"Out of nowhere... {loser.finisher}!",
                f"Finally catching {winner.name} off-guard, {loser.name} connects with the {loser.finisher}!",
                f"The crowd is roaring, seeing what is coming! {loser.finisher}! Yes! {loser.name} hits it!!!"
            ],
            "Grapple": [
                f"{loser.name} gathers himself and picks {winner.name} up... {loser.finisher}!",
                f"Taking a deep breath, {loser.name} sets up. Nails the {loser.finisher}! {winner.name} slams to the mat!",
                f"The crowd sees what's happening and starts to boo. {loser.name} goes for the {loser.finisher}. Got it! {winner.name} is out cold!!"
            ]
        },
        "winner": {
            "Standing": [
                f"Out of nowhere... {winner.finisher}!",
                f"Finally catching {loser.name} off-guard, {winner.name} connects with the {winner.finisher}!",
                f"The crowd is roaring, seeing what is coming! {winner.finisher}! Yes! {winner.name} hits it!!!"
            ],
            "Grapple": [
                f"{winner.name} gathers himself and picks {loser.name} up... {winner.finisher}!",
                f"Taking a deep breath, {winner.name} sets up. Nails the {winner.finisher}! {loser.name} slams to the mat!",
                f"The crowd sees what's happening and starts to boo. {winner.name} goes for the {winner.finisher}. Got it! {loser.name} is out cold!!"
            ]
        }
    }

    # Get the correct list based on edge and finishertype
    finisher_list = finisher_scenarios[edge][loser.finishertype if edge == "loser" else winner.finishertype]


    print(random.choice(finisher_list))
    return edge


def endMatch(winner, loser, edge):
    standardpin = [
        f"{winner.name} goes for the pin and hooks the leg!  1!  2!  3!!!",
        f"Exhausted, {winner.name} drops to his knees and covers {loser.name}.  1...2... 3!!!"
    ]
    surprisepin = [
        f"{loser.name} shows off to the crowd and goes to cover.  WAIT!  {winner.name} rolls {loser.name} up for a pin!  1! 2! 3!!",
        f"Playing possum, {winner.name} catches {loser.name} off-guard and rolls him up!  1.. 2.. 3!!!"
    ]

    if edge == "loser":
        print(random.choice(surprisepin))
    else:
        print(random.choice(standardpin))

