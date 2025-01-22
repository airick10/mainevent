from random import randrange
import random
import time

class Match:
    def __init__(self, winner, loser, matchTime, finisherKickout):
        self.winner = winner
        self.loser = loser
        self.edge = "winner"
        self.matchTime = matchTime
        self.finisherKickout = finisherKickout


    def matchDirector(self):
        matchCounter = 1
        while self.matchTime > matchCounter:
            if matchCounter == 1:
                self.startMatch()
                time.sleep(1)
            else:
                midRand = random.randrange(100)
                #General mid match moves
                if midRand <= 60:
                    self.midMatch()
                    time.sleep(1)
                #Climing to the top rope
                elif midRand > 60 and midRand < 81:
                    self.midMatch()
                    self.topRopeRing()
                    time.sleep(1)
                #Throwing the opponent to the outside
                else:
                    self.throwToOutside()
                if random.randrange(100) > 50:
                    self.crowdReaction()
            if ((self.matchTime - matchCounter) < 4) and random.randrange(100) < 35:
                matchCounter = self.matchTime
            matchCounter += 1
        self.finisherStage()   

    def startMatch(self):
        start = random.randrange(100)
        if start < 20:
            print(f"{self.loser.name} starts out on fire rushing {self.winner.name} with a flurry of punches!")
            self.edge = "loser"
        elif start < 60:
            print(f"Both fighters stare at each other. Slowly walking towards the center and gauge each other.")
            self.edge = "winner"
        else:
            print(f"{self.winner.name} dodges a punch and whips {self.loser.name} to the corner. He follows and starts to deliver a series of punches to {self.loser.name}!")
            self.edge = "winner"


    def crowdReaction(self):
        crowd_reaction = {
                "loser": {
                    "Face": [
                        f"The crowd erupts!  They love every minute of this!!",
                        f"{self.loser.name} takes in the praise from the crowd and gets them cheering!  The fans love it!",
                        f"Chanting praising {self.loser.name} are heard from the crowd!  This place is getting loud!"
                    ],
                    "Heel": [
                        f"Echoes of boos are heard as {self.loser.name} ignores them and keeps pressing on.",
                        f"Moans and groans are heard from the crowd.  They don't like what they are seeing at all.",
                        f"Somehow, {self.loser.name} is really enjoying hearding these boos and jeers from the crowd."
                    ]
                },
                "winner": {
                    "Face": [
                        f"The crowd erupts!  They love every minute of this!!",
                        f"{self.winner.name} takes in the praise from the crowd and gets them cheering!  The fans love it!",
                        f"Chanting praising {self.winner.name} are heard from the crowd!  This place is getting loud!"
                    ],
                    "Heel": [
                        f"Echoes of boos are heard as {self.winner.name} ignores them and keeps pressing on.",
                        f"Moans and groans are heard from the crowd.  They don't like what they are seeing at all.",
                        f"Somehow, {self.winner.name} is really enjoying hearding these boos and jeers from the crowd."
                    ]
                }
            }

        align_key = "Face" if (self.winner.align if self.edge == "winner" else self.loser.align) > 50 else "Heel"

        reaction_list = crowd_reaction[self.edge][align_key]

        print(random.choice(reaction_list))

    def midMatch(self):
        if random.randrange(100) < 30:
            self.reversal()
            time.sleep(1)
            if random.randrange(100) < 15:
                self.suddenFinisher()
                time.sleep(1)
        else:
            match_moves = {
                "loser": {
                    "Powerhouse": [
                        f"{self.loser.name} whips {self.winner.name} along the ropes!  Thunderous Powerslam!",
                        f"{self.loser.name} picks {self.winner.name} up quickly and slams him to the ground like a rag doll! ",
                        f"Look at this!  {self.loser.name} is licking his chops.  He picks up {self.winner.name} with both hands and delivers a double choke slam!",
                        f"{self.loser.name} charges at {self.winner.name}, flattening him with a running shoulder block!",
                        f"{self.loser.name} hoists {self.winner.name} onto his shoulder and plants him with a devastating powerslam!",
                        f"{self.loser.name} catches {self.winner.name} mid-air and slams him down with a spine-crunching backbreaker!",
                        f"{self.loser.name} grabs {self.winner.name} by the arm and yanks him into a thunderous short-arm clothesline!"
                    ],
                    "All-Around": [
                        f"{self.loser.name} kicks him in the gut...  DDT!  {self.winner.name} drops to the mat!",
                        f"After a knee to the gut, {self.loser.name} slips around... runs up and drops a bulldog!",
                        f"{self.loser.name} flings {self.winner.name} to the ropes.  {self.loser.name} catches him in a fallaway slam!",
                        f"{self.loser.name} surprises {self.winner.name} with a snap suplex! Smooth execution!",
                        f"{self.loser.name} counters {self.winner.name}'s attack with a quick drop toe hold and transitions into a headlock!",
                        f"{self.loser.name} springboards off the ropes and catches {self.winner.name} with a crossbody!",
                        f"{self.loser.name} flips over {self.winner.name} in a sunset flip attempt! The ref slides in for a two-count!"
                    ],
                    "Brawler": [
                        f"{self.loser.name} finishes a few punches with a dynamite clothesline!  Wow, what force!",
                        f"{self.loser.name} throws {self.winner.name} to the ropes and connects with an elbow knocking {self.winner.name} down hard!",
                        f"{self.loser.name} fires a punch!  And another!  Brings {self.winner.name} to his knees!  {self.loser.name} drops down a double ax handle!",
                        f"{self.loser.name} unleashes a flurry of rights and lefts, driving {self.winner.name} back into the corner!",
                        f"{self.loser.name} grabs {self.winner.name}'s head and repeatedly rams it into the turnbuckle!",
                        f"{self.loser.name} levels {self.winner.name} with a stiff knee to the midsection, followed by a running boot!",
                        f"{self.loser.name} hooks {self.winner.name}'s head and lands a rough neckbreaker!"
                    ]
                },
                "winner": {
                    "Powerhouse": [
                        f"{self.winner.name} whips {self.loser.name} along the ropes!  Thunderous Powerslam!",
                        f"{self.winner.name} picks {self.loser.name} up quickly and slams him to the ground like a rag doll! ",
                        f"Look at this!  {self.winner.name} is licking his chops.  He picks up {self.loser.name} with both hands and delivers a double choke slam!",
                        f"{self.winner.name} grabs {self.loser.name} in a bearhug and squeezes the life out of him!",
                        f"{self.winner.name} scoops up {self.loser.name} and slams him down with an earth-shaking body slam!",
                        f"{self.winner.name} picks {self.loser.name} up like a feather and hits a massive powerbomb!",
                        f"{self.winner.name} lifts {self.loser.name} in a military press, holding him high before slamming him to the mat!"
                    ],
                    "All-Around": [
                        f"{self.winner.name} kicks him in the gut...  DDT!  {self.loser.name} drops to the mat!",
                        f"After a knee to the gut, {self.winner.name} slips around... runs up and drops a bulldog!",
                        f"{self.winner.name} flings {self.loser.name} to the ropes.  {self.winner.name} catches him in a fallaway slam!",
                        f"{self.winner.name} ducks under a clothesline and counters with a perfect German suplex!",
                        f"{self.winner.name} climbs to the top rope and nails {self.loser.name} with a flying elbow drop!",
                        f"{self.winner.name} grabs {self.loser.name}'s arm and pulls him into a picture-perfect arm drag!",
                        f"{self.winner.name} counters {self.loser.name}'s move with a sharp enzuigiri to the back of the head!"
                    ],
                    "Brawler": [
                        f"{self.winner.name} finishes a few punches with a dynamite clothesline!  Wow, what force!",
                        f"{self.winner.name} throws {self.loser.name} to the ropes and connects with an elbow knocking {self.loser.name} down hard!",
                        f"{self.winner.name} fires a punch!  And another!  Brings {self.loser.name} to his knees!  {self.winner.name} drops down a double ax handle!",
                        f"{self.winner.name} pounds on {self.loser.name} with a relentless series of punches, driving him to the ground!",
                        f"{self.winner.name} connects with a brutal headbutt, sending {self.loser.name} staggering!",
                        f"{self.winner.name} traps {self.loser.name} in the corner and unloads with machine-gun-like punches!",
                        f"{self.winner.name} catches {self.loser.name}'s kick and drops him with a dragon screw leg whip!"
                    ]
                }
            }

            match_list = match_moves[self.edge][self.loser.style if self.edge == "loser" else self.winner.style]

            print(random.choice(match_list))

            self.groundedMidMatch()

        if random.randrange(100) < 20:
            self.failedPin("Standard")



    def reversal(self):
        loserreversals = [
            f"Oh! What a reversal by {self.loser.name}!",
            f"{self.winner.name} tries to deliver a crushing blow, but {self.loser.name} reverses it beautifully!",
            f"{self.loser.name} counters with a stunning suplex on {self.winner.name}!",
            f"{self.loser.name} ducks under a clothesline and delivers a dropkick to {self.winner.name}!",
            f"{self.loser.name} reverses a grapple and sends {self.winner.name} crashing to the mat with a back body drop!",
            f"The crowd roars as {self.loser.name} counters with a jaw-dropping reversal!",
            f"{self.loser.name} sidesteps and slams {self.winner.name} into the turnbuckle!",
            f"{self.loser.name} catches {self.winner.name}'s arm and locks in a quick armbar before letting go!"
        ]
        winnerreversals = [
            f"Oh! What a reversal by {self.winner.name}!",
            f"{self.loser.name} tries to deliver a crushing blow, but {self.winner.name} reverses it beautifully!",
            f"{self.winner.name} counters with a stunning suplex on {self.loser.name}!",
            f"{self.winner.name} ducks under a clothesline and delivers a dropkick to {self.loser.name}!",
            f"{self.winner.name} reverses a grapple and sends {self.loser.name} crashing to the mat with a back body drop!",
            f"The crowd roars as {self.winner.name} counters with a jaw-dropping reversal!",
            f"{self.winner.name} sidesteps and slams {self.loser.name} into the turnbuckle!",
            f"{self.winner.name} catches {self.loser.name}'s arm and locks in a quick armbar before letting go!"
        ]

        if self.edge == "loser":
            print(random.choice(winnerreversals))
            self.edge = "winner"
        else:
            print(random.choice(loserreversals))
            self.edge = "loser"


    def topRopeRing(self):
        if random.randrange(100) < 30:
            if self.edge == "loser":
                print(f"{self.loser.name} climbs up the turnbuckle!  Measures... flies through the air!  Oh!  {self.winner.name} rolls out of the way!!")
                self.edge = "winner"
            if self.edge == "winner":
                print(f"{self.winner.name} climbs up the turnbuckle!  Measures... flies through the air!  Oh!  {self.loser.name} rolls out of the way!!")
                self.edge = "loser"
        else:
            toprope_moves = {
                "loser": {
                    "Powerhouse": [
                        f"Look at this! {self.loser.name} is crawling up the top rope!  He delivers a flying fist drop!  Who knew he could fly through the air?",
                        f"Step-by-step, {self.loser.name} climbs up the top rope.  I can't believe it.  He flies!  Oh!! Giant body splash!"
                    ],
                    "All-Around": [
                        f"As {self.winner.name} lays on the mat, {self.loser.name} jumps up the top turn buckle.  Soars through the air!  What a leg drop!",
                        f"{self.loser.name} grabs the turnbuckle and hoists himself up.  Turns around, measures... flies and delivers a flying elbow!!",
                        f"{self.winner.name} looks helpless on the mat as {self.loser.name} climbs up the turnbuckle.  Looks around to the crowd.  OH!! A beautiful moonsault!!",
                        f"{self.loser.name} is pumped up!  He climbs up the turnbuckle, points at {self.winner.name} on the mat. What a flying frog splash!  WHAM!!"
                    ],
                    "Brawler": [
                        f"Looking knocked out, {self.winner.name} lays on his back as {self.loser.name} climbs up the top rope.  Flies!  Oh!!  What a fist drop!!",
                        f"{self.loser.name} eyes the turnbuckle.  Climbs up and pats his elbow.  Jumps and lands a giant elbow drop right on the chest of {self.winner.name}!!",
                        f"Running to the turn buckle, {self.loser.name} hops up... stands tall... jumps and lands a flying leg drop right across the throat of {self.winner.name}!",
                        f"Wow!  Look at {self.loser.name}!! He's climbing up the turnbuckle.  Flies through the hair and lands a devistating fist drop!  My oh my!!"
                    ]
                },
                "winner": {
                    "Powerhouse": [
                        f"Look at this! {self.winner.name} is crawling up the top rope!  He delivers a flying fist drop!  Who knew he could fly through the air?",
                        f"Step-by-step, {self.winner.name} climbs up the top rope.  I can't believe it.  He flies!  Oh!! Giant body splash!"
                    ],
                    "All-Around": [
                        f"As {self.loser.name} lays on the mat, {self.winner.name} jumps up the top turn buckle.  Soars through the air!  What a leg drop!",
                        f"{self.winner.name} grabs the turnbuckle and hoists himself up.  Turns around, measures... flies and delivers a flying elbow!!",
                        f"{self.loser.name} looks helpless on the mat as {self.winner.name} climbs up the turnbuckle.  Looks around to the crowd.  OH!! A beautiful moonsault!!",
                        f"{self.winner.name} is pumped up!  He climbs up the turnbuckle, points at {self.loser.name} on the mat. What a flying frog splash!  WHAM!!"
                    ],
                    "Brawler": [
                        f"Looking knocked out, {self.loser.name} lays on his back as {self.winner.name} climbs up the top rope.  Flies!  Oh!!  What a fist drop!!",
                        f"{self.winner.name} eyes the turnbuckle.  Climbs up and pats his elbow.  Jumps and lands a giant elbow drop right on the chest of {self.loser.name}!!",
                        f"Running to the turn buckle, {self.winner.name} hops up... stands tall... jumps and lands a flying leg drop right across the throat of {self.loser.name}!",
                        f"Wow!  Look at {self.winner.name}!! He's climbing up the turnbuckle.  Flies through the hair and lands a devistating fist drop!  My oh my!!"
                    ]
                }
            }

            toprope_list = toprope_moves[self.edge][self.loser.style if self.edge == "loser" else self.winner.style]

            print(random.choice(toprope_list))

        if random.randrange(100) < 20:
            self.failedPin("Standard")

        self.groundedMidMatch()



    def throwToOutside(self):

        loseroutside = [
            f"{self.loser.name} flings {self.winner.name} along the ropes... tosses {self.winner.name} to the outside!  {self.loser.name} follows him to the outside.",
            f"{self.winner.name} manages to make his way to the edge of the ropes.  {self.loser.name} quickly rushes and clotheslines him out of the ring!"
        ]
        winneroutside = [
            f"{self.winner.name} flings {self.loser.name} along the ropes... tosses {self.loser.name} to the outside!  {self.winner.name} follows him to the outside.",
            f"{self.loser.name} manages to make his way to the edge of the ropes.  {self.winner.name} quickly rushes and clotheslines him out of the ring!"
        ]

        if self.edge == "loser":
            print(random.choice(loseroutside))
        else:
            print(random.choice(winneroutside))

        counter = 1

        while counter < 4:
            if random.randrange(100) < 30:
                self.reversal()
                time.sleep(1)
            else:
                match_moves = {
                    "loser": {
                        "Powerhouse": [
                            f"{self.loser.name} picks {self.winner.name} up and quickly whips him along the post!  Ouch!",
                            f"{self.loser.name} stomps on {self.winner.name} a couple times and picks him up.  Body Slam on the concrete!!",
                            f"{self.loser.name} helps {self.winner.name} to his feet and rams him along the barricade!  {self.winner.name} holds his chest in pain!",
                            f"Flexing a bit, {self.loser.name} picks up {self.winner.name} and body presses him!  Drops {self.winner.name} down on the concrete!  Wow!"
                        ],
                        "All-Around": [
                            f"After catching his breath a bit, {self.loser.name} picks up {self.winner.name} and starts delivering a few punches dropping {self.winner.name} to the concrete!",
                            f"{self.loser.name} helps {self.winner.name} to his feet, positions... delivers a suplex onto the concrete!  That has to be painful!",
                            f"As {self.winner.name} gets up, {self.loser.name} quickly grabs him and whips him to the barricade.  Follows up with a running knee!!",
                            f"{self.loser.name} whips {self.winner.name} along the rideside steps!! {self.winner.name} tumbles over them holding his legs!!  Ouch!!"
                        ],
                        "Brawler": [
                            f"Waiting for {self.winner.name} to get up, {self.loser.name} delivers a solid punch that knocks {self.winner.name} to the concrete as he rolls around a bit.",
                            f"Without waiting for {self.winner.name} to get to his feet, {self.loser.name} stomps away on {self.winner.name}!  That can't feel good on that concrete!!",
                            f"{self.loser.name} picks up {self.winner.name}, grabs him and delivers a german suplex!!  Right on that hard concrete!!",
                            f"{self.loser.name} drops an elbow on {self.winner.name} on the outside.  He gets up, picks up {self.winner.name} and quickly body slams him!"
                        ]
                    },
                    "winner": {
                        "Powerhouse": [
                            f"{self.winner.name} picks {self.loser.name} up and quickly whips him along the post!  Ouch!",
                            f"{self.winner.name} stomps on {self.loser.name} a couple times and picks him up.  Body Slam on the concrete!!",
                            f"{self.winner.name} helps {self.loser.name} to his feet and rams him along the barricade!  {self.loser.name} holds his chest in pain!",
                            f"Flexing a bit, {self.winner.name} picks up {self.loser.name} and body presses him!  Drops {self.loser.name} down on the concrete!  Wow!"
                        ],
                        "All-Around": [
                            f"After catching his breath a bit, {self.winner.name} picks up {self.loser.name} and starts delivering a few punches dropping {self.loser.name} to the concrete!",
                            f"{self.winner.name} helps {self.loser.name} to his feet, positions... delivers a suplex onto the concrete!  That has to be painful!",
                            f"As {self.loser.name} gets up, {self.winner.name} quickly grabs him and whips him to the barricade.  Follows up with a running knee!!",
                            f"{self.winner.name} whips {self.loser.name} along the rideside steps!! {self.loser.name} tumbles over them holding his legs!!  Ouch!!"
                        ],
                        "Brawler": [
                            f"Waiting for {self.loser.name} to get up, {self.winner.name} delivers a solid punch that knocks {self.loser.name} to the concrete as he rolls around a bit.",
                            f"Without waiting for {self.loser.name} to get to his feet, {self.winner.name} stomps away on {self.loser.name}!  That can't feel good on that concrete!!",
                            f"{self.winner.name} picks up {self.loser.name}, grabs him and delivers a german suplex!!  Right on that hard concrete!!",
                            f"{self.winner.name} drops an elbow on {self.loser.name} on the outside.  He gets up, picks up {self.loser.name} and quickly body slams him!"
                        ]
                    }
                }

                match_list = match_moves[self.edge][self.loser.style if self.edge == "loser" else self.winner.style]

                print(random.choice(match_list))
                if random.randrange(100) <= 50:
                    counter = 4

            counter += 1

        if self.edge == "loser":
            print(f"{self.loser.name} rolls back into the ring and awaits {self.winner.name} to climb back in.")
        else:
            print(f"{self.winner.name} rolls back into the ring and awaits {self.loser.name} to climb back in.")



    def groundedMidMatch(self):
        if random.randrange(100) < 30:
            self.reversalGrounded()
            time.sleep(1)
        else:
            ground_moves = {
                "loser": {
                    "Powerhouse": [
                        f"{self.loser.name} drops a giant elbow on {self.winner.name}!  He slowly picks {self.winner.name} up.",
                        f"Big Splash!  Ouch! {self.loser.name} comes down hard on {self.winner.name}!  Can he even breathe?  {self.winner.name} eventually gets up",
                        f"{self.loser.name} bounces off the ropes and slowly drops a giant leg drop across the throat of {self.winner.name}!  {self.loser.name} brings {self.winner.name} to his feet."
                    ],
                    "All-Around": [
                        f"{self.loser.name} picks up {self.winner.name}'s leg and drops and elbow on the knee!  {self.winner.name} grabs his leg in pain!  {self.loser.name} allows {self.winner.name} to get up.",
                        f"Stomping away... {self.loser.name} keeps kicking {self.winner.name} on the ground and then brings him to his feet.",
                        f"Flinging himself off the ropes, {self.loser.name} drops an elbow to the heart of {self.winner.name}!  {self.winner.name} eventually gets to his feet holding his chest."
                    ],
                    "Brawler": [
                        f"{self.loser.name} sits on top of {self.winner.name} and delivers blow after blow and gets up.  He waits for {self.winner.name} to get to his feet.",
                        f"{self.loser.name} stomps away at {self.winner.name} on the mat!  He bends down and brings {self.winner.name} to his feet.",
                        f"{self.loser.name} drops an elbow and gets up and again and drops another one!  {self.winner.name} rolls around in pain and eventually gets up"
                    ]
                },
                "winner": {
                    "Powerhouse": [
                        f"{self.winner.name} drops a giant elbow on {self.loser.name}!  He slowly picks {self.loser.name} up.",
                        f"Big Splash!  Ouch! {self.winner.name} comes down hard on {self.loser.name}!  Can he even breathe?  {self.loser.name} eventually gets up",
                        f"{self.winner.name} bounces off the ropes and slowly drops a giant leg drop across the throat of {self.loser.name}!  {self.winner.name} brings {self.loser.name} to his feet."
                    ],
                    "All-Around": [
                        f"{self.winner.name} picks up {self.loser.name}'s leg and drops and elbow on the knee!  {self.loser.name} grabs his leg in pain!  {self.winner.name} allows {self.loser.name} to get up.",
                        f"Stomping away... {self.winner.name} keeps kicking {self.loser.name} on the ground and then brings him to his feet.",
                        f"Flinging himself off the ropes, {self.winner.name} drops an elbow to the heart of {self.loser.name}!  {self.loser.name} eventually gets to his feet holding his chest."
                    ],
                    "Brawler": [
                        f"{self.winner.name} sits on top of {self.loser.name} and delivers blow after blow and gets up.  He waits for {self.loser.name} to get to his feet.",
                        f"{self.winner.name} stomps away at {self.loser.name} on the mat!  He bends down and brings {self.loser.name} to his feet.",
                        f"{self.winner.name} drops an elbow and gets up and again and drops another one!  {self.loser.name} rolls around in pain and eventually gets up"
                    ]
                }
            }

            ground_list = ground_moves[self.edge][self.loser.style if self.edge == "loser" else self.winner.style]

            print(random.choice(ground_list))
        if random.randrange(100) < 20:
            self.failedPin("Standard")



    def reversalGrounded(self):
        loserreversals = [
            f"{self.loser.name} rolls out of the way as {self.winner.name} tries to drop an elbow!  {self.loser.name} quickly gets to his feet!",
            f"{self.winner.name} goes to pick up {self.loser.name}, but is met with a punch to the gut stunning {self.winner.name}!",
            f"On the mat, {self.loser.name} sweeps the leg of {self.winner.name} as he approaches!  What a reversal!  {self.loser.name} gets to his feet!"
        ]
        winnerreversals = [
            f"{self.winner.name} rolls out of the way as {self.loser.name} tries to drop an elbow!  {self.winner.name} quickly gets to his feet!",
            f"{self.loser.name} goes to pick up {self.winner.name}, but is met with a punch to the gut stunning {self.loser.name}!",
            f"On the mat, {self.winner.name} sweeps the leg of {self.loser.name} as he approaches!  What a reversal!  {self.winner.name} gets to his feet!"
        ]

        if self.edge == "loser":
            print(random.choice(winnerreversals))
        else:
            print(random.choice(loserreversals))


    def suddenFinisher(self):
        sudden_finisher_scenarios = {
            "loser": {
                "Standing": [
                    f"Out of nowhere... {self.loser.finisher}!",
                    f"Finally catching {self.winner.name} off-guard, {self.loser.name} connects with the {self.loser.finisher}!",
                    f"The crowd is roaring, seeing what is coming! {self.loser.finisher}! Yes! {self.loser.name} hits it!!!"
                ],
                "Grapple": [
                    f"{self.loser.name} gathers himself and picks {self.winner.name} up... {self.loser.finisher}!",
                    f"Taking a deep breath, {self.loser.name} sets up. Nails the {self.loser.finisher}! {self.winner.name} slams to the mat!",
                    f"The crowd sees what's happening and starts to boo. {self.loser.name} goes for the {self.loser.finisher}. Got it! {self.winner.name} is out cold!!"
                ]
            },
            "winner": {
                "Standing": [
                    f"Out of nowhere... {self.winner.finisher}!",
                    f"Finally catching {self.loser.name} off-guard, {self.winner.name} connects with the {self.winner.finisher}!",
                    f"The crowd is roaring, seeing what is coming! {self.winner.finisher}! Yes! {self.winner.name} hits it!!!"
                ],
                "Grapple": [
                    f"{self.winner.name} gathers himself and picks {self.loser.name} up... {self.winner.finisher}!",
                    f"Taking a deep breath, {self.winner.name} sets up. Nails the {self.winner.finisher}! {self.loser.name} slams to the mat!",
                    f"The crowd sees what's happening and starts to boo. {self.winner.name} goes for the {self.winner.finisher}. Got it! {self.loser.name} is out cold!!"
                ]
            }
        }

        # Get the correct list based on edge and finishertype
        finisher_list = sudden_finisher_scenarios[self.edge][self.loser.finishertype if self.edge == "loser" else self.winner.finishertype]

        print(random.choice(finisher_list))


    def failedPin(self,stage):
        pin_scenarios = {
            "loser": {
                "Standard": [
                    f"{self.loser.name} goes for the pin... 1!  2!  No!  {self.winner.name} gets a shoulder up!",
                    f"{self.winner.name} is on the mat!  {self.loser.name} tries to go for the win!  1..  2... Kick out!",
                    f"{self.loser.name} sees a downed {self.winner.name} and goes for the pin.  Hooks the leg!  1...  2...  No! That's just two!"
                ],
                "Finisher": [
                    f"{self.loser.name} smiles knowing he's got this win!  Goes for the pin...  1...  2...   NO!! MY GOD!  He kicked out!!  {self.loser.name} is stunned!",
                    f"{self.loser.name} goes for the pin... 1!  2!  No!  {self.winner.name} gets a shoulder up!  How did he do that??",
                    f"Oh this has got to be it.  {self.loser.name} pins {self.winner.name}.  1!  2!  KICK OUT!! WOW!!!"
                ]
            },
            "winner": {
                "Standard": [
                    f"{self.winner.name} goes for the pin... 1!  2!  No!  {self.loser.name} gets a shoulder up!",
                    f"{self.loser.name} is on the mat!  {self.winner.name} tries to go for the win!  1..  2... Kick out!",
                    f"{self.winner.name} sees a downed {self.loser.name} and goes for the pin.  Hooks the leg!  1...  2...  No! That's just two!"
                ],
                "Finisher": [
                    f"{self.winner.name} smiles knowing he's got this win!  Goes for the pin...  1...  2...   NO!! MY GOD!  He kicked out!!  {self.winner.name} is stunned!",
                    f"{self.winner.name} goes for the pin... 1!  2!  No!  {self.loser.name} gets a shoulder up!  How did he do that??",
                    f"Oh this has got to be it.  {self.winner.name} pins {self.loser.name}.  1!  2!  KICK OUT!! WOW!!!"
                ]
            }
        }

        pin_list = pin_scenarios[self.edge][stage]

        print(random.choice(pin_list))

        if random.randrange(100) < 30:
            self.reversalGrounded()


    def reversalFinisher(self):
        finisher_scenarios = {
                "loser": {
                    "Standing": [
                        f"Taking a deep breath, {self.loser.name} catches the stunned {self.winner.name} and goes for the {self.winner.finisher}!  NO!  {self.winner.name} counters!",
                        f"Oh, it's all set up now!  {self.loser.name} gets ready and whiffs on the {self.loser.finisher}!  {self.winner.name} dodges and regroups",
                        f"A bit woozy and dazed, {self.winner.name} turns around to see {self.loser.name} waiting.  OH! {self.winner.name} catches {self.loser.name} trying for the {self.loser.finisher}!  Countered!"
                    ],
                    "Grapple": [
                        f"{self.loser.name} gathers himself and picks {self.winner.name} up... Tries for the {self.loser.finisher}!  {self.winner.finisher} fights out of it!  Wow!  Knocks {self.loser.name} on the counter!",
                        f"Taking a deep breath, {self.loser.name} sets up. Goes for the {self.loser.finisher}! {self.winner.name}... being sly and cunning... easily counters!",
                        f"{self.loser.name} goes for the {self.loser.finisher}. No!! {self.winner.name} escapes the devestating move and counters!"
                    ]
                }
            }

        
        finisher_list = finisher_scenarios["loser"][self.loser.finishertype]
        print(random.choice(finisher_list))
        self.edge = "winner"
        self.finisherStage()


    def finisherStage(self):
        finishLoop = True
        while finishLoop:
            if self.edge == "loser":
                self.reversalFinisher()
                time.sleep(1)
            else:
                finisher_scenarios = {
                    "winner": {
                        "Standing": [
                            f"Taking a deep breath, {self.winner.name} catches the stunned {self.loser.name} and connects with {self.winner.finisher}!  Oh what a move!!",
                            f"Oh, it's all set up now!  {self.winner.name} gets ready and nails {self.loser.name} with a devestating {self.winner.finisher}!  No way he gets up from this!",
                            f"A bit woozy and dazed, {self.loser.name} turns around to see {self.winner.name} waiting.  OH! {self.winner.finisher}!  This has got to be over now!!"
                        ],
                        "Grapple": [
                            f"{self.winner.name} gathers himself and picks {self.loser.name} up... {self.winner.finisher}!",
                            f"Taking a deep breath, {self.winner.name} sets up. Nails the {self.winner.finisher}! {self.loser.name} slams to the mat!",
                            f"{self.winner.name} goes for the {self.winner.finisher}. Got it! {self.loser.name} is out cold!!"
                        ]
                    }
                }

                # Get the correct list based on edge and finishertype
                finisher_list = finisher_scenarios["winner"][self.winner.finishertype]
                print(random.choice(finisher_list))
            if self.finisherKickout and random.randrange(100) < 20:
                self.failedPin("Finisher")
                self.finisherKickout = False
            else:
                finishLoop = False

        self.endMatch()
        finishLoop = False


    def endMatch(self):
        standardpin = [
            f"{self.winner.name} goes for the pin and hooks the leg!  1!  2!  3!!!",
            f"Exhausted, {self.winner.name} drops to his knees and covers {self.loser.name}.  1...2... 3!!!"
        ]
        surprisepin = [
            f"{self.loser.name} shows off to the crowd and goes to cover.  WAIT!  {self.winner.name} rolls {self.loser.name} up for a pin!  1! 2! 3!!",
            f"Playing possum, {self.winner.name} catches {self.loser.name} off-guard and rolls him up!  1.. 2.. 3!!!"
        ]

        if self.edge == "loser":
            print(random.choice(surprisepin))
        else:
            print(random.choice(standardpin))

        if self.winner.align >= 80:
            print(f"The crowd explodes!! {self.winner.name} celebrates with the crowd!")
        elif self.winner.align >= 50 and self.winner.align < 80:
            print(f"{self.winner.name} is greeted by a cheers and applause by the crowd!")
        elif self.winner.align < 50 and self.winner.align > 20:
            print(f"{self.winner.name} relishes in the groans heard in the crowd.  They aren't happy with this win.")
        else:
            print(f"Loud boos and jeers are heard from the fans.  {self.winner.name} taunts them in celebration!  He won't win them over that way.")