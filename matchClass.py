from random import randrange
import random
import time
import json

class Match:
    def __init__(self, winner, loser, matchTime, finisherKickout):
        self.winner = winner
        self.loser = loser
        self.edge = "winner"
        self.matchTime = matchTime
        self.finisherKickout = finisherKickout

    def load_data(self, file_path):
        try:
            with open(file_path, 'r') as file:
                self.data = json.load(file)
        except FileNotFoundError:
            raise ValueError(f"File not found: {file_path}")
        except json.JSONDecodeError:
            raise ValueError(f"Invalid JSON format in file: {file_path}")


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


    def getActionString(self, dataKey, subKey):
        record_list = self.data[dataKey][self.edge][subKey]
        return random.choice([
            record.format(
                winner=self.winner.name,
                loser=self.loser.name,
                winner_finisher=self.winner.finisher,
                loser_finisher=self.loser.finisher
            )
            for record in record_list
        ])
   

    def output(self, message):
        #Future function. Can be redirected to a file or GUI
        print(message)

    def is_face(self, wrestler) -> bool:
        return wrestler.align > 50

    def is_heel(self, wrestler) -> bool:
        return wrestler.align <= 50

    def startMatch(self):
        start = random.randrange(100)
        if start < 20:
            self.output(f"{self.loser.name} starts out on fire rushing {self.winner.name} with a flurry of punches!")
            self.edge = "loser"
        elif start < 60:
            self.output(f"Both fighters stare at each other. Slowly walking towards the center and gauge each other.")
            self.edge = "winner"
        else:
            self.output(f"{self.winner.name} dodges a punch and whips {self.loser.name} to the corner. He follows and starts to deliver a series of punches to {self.loser.name}!")
            self.edge = "winner"


    def crowdReaction(self):
        align_key = "Face" if self.is_face(self.winner if self.edge == "winner" else self.loser) else "Heel"

        record_list = self.data["crowd_reaction"][self.edge][align_key]
        records = [record.format(winner=self.winner.name, loser=self.loser.name) for record in record_list]

        self.output(random.choice(records))

    def midMatch(self):
        if random.randrange(100) < 30:
            self.reversal()
            time.sleep(1)
            if random.randrange(100) < 15:
                self.suddenFinisher()
                time.sleep(1)
        else:
            self.output(self.getActionString("match_moves", self.winner.style if self.edge == "winner" else self.loser.style))

            self.groundedMidMatch()

        if random.randrange(100) < 20:
            self.failedPin("Standard")



    def reversal(self):
        loser_reversals = self.data["loser_reversals"]
        loser_formatted = [record.format(winner=self.winner.name, loser=self.loser.name) for record in loser_reversals]
        winner_reversals = self.data["winner_reversals"]
        winner_formatted = [record.format(winner=self.winner.name, loser=self.loser.name) for record in winner_reversals]

        if self.edge == "loser":
            self.output(random.choice(winner_formatted))
            self.edge = "winner"
        else:
            self.output(random.choice(loser_formatted))
            self.edge = "loser"


    def topRopeRing(self):
        if random.randrange(100) < 30:
            if self.edge == "loser":
                self.output(f"{self.loser.name} climbs up the turnbuckle!  Measures... flies through the air!  Oh!  {self.winner.name} rolls out of the way!!")
                self.edge = "winner"
            if self.edge == "winner":
                self.output(f"{self.winner.name} climbs up the turnbuckle!  Measures... flies through the air!  Oh!  {self.loser.name} rolls out of the way!!")
                self.edge = "loser"
        else:
            self.output(self.getActionString("toprope_moves", self.winner.style if self.edge == "winner" else self.loser.style))

        if random.randrange(100) < 20:
            self.failedPin("Standard")

        self.groundedMidMatch()



    def throwToOutside(self):
        loser_outside = self.data["loseroutside"]
        loser_formatted = [record.format(winner=self.winner.name, loser=self.loser.name) for record in loser_outside]
        winner_outside = self.data["winneroutside"]
        winner_formatted = [record.format(winner=self.winner.name, loser=self.loser.name) for record in winner_outside]

        if self.edge == "loser":
            self.output(random.choice(loser_formatted))
        else:
            self.output(random.choice(winner_formatted))

        counter = 1

        while counter < 4:
            if random.randrange(100) < 30:
                self.reversal()
                time.sleep(1)
            else:
                self.output(self.getActionString("match_moves_outside", self.winner.style if self.edge == "winner" else self.loser.style))

                if random.randrange(100) <= 50:
                    counter = 4

            counter += 1

        if self.edge == "loser":
            self.output(f"{self.loser.name} rolls back into the ring and awaits {self.winner.name} to climb back in.")
        else:
            self.output(f"{self.winner.name} rolls back into the ring and awaits {self.loser.name} to climb back in.")



    def groundedMidMatch(self):
        if random.randrange(100) < 30:
            self.reversalGrounded()
            time.sleep(1)
        else:
            self.output(self.getActionString("ground_moves", self.winner.style if self.edge == "winner" else self.loser.style))
        if random.randrange(100) < 20:
            self.failedPin("Standard")



    def reversalGrounded(self):
        loser_ground = self.data["loser_reversals_ground"]
        loser_formatted = [record.format(winner=self.winner.name, loser=self.loser.name) for record in loser_ground]
        winner_ground = self.data["winner_reversals_ground"]
        winner_formatted = [record.format(winner=self.winner.name, loser=self.loser.name) for record in winner_ground]

        if self.edge == "loser":
            self.output(random.choice(winner_formatted))
        else:
            self.output(random.choice(loser_formatted))


    def suddenFinisher(self):
        self.output(self.getActionString("sudden_finisher_scenarios", self.winner.finishertype if self.edge == "winner" else self.loser.finishertype))


    def failedPin(self,stage):
        record_list = self.data["pin_scenarios"][self.edge][stage]
        records = [record.format(winner=self.winner.name, loser=self.loser.name) for record in record_list]

        self.output(random.choice(records))

        if random.randrange(100) < 30:
            self.reversalGrounded()


    def reversalFinisher(self):
        self.output(self.getActionString("reversal_finisher_scenarios", self.winner.finishertype if self.edge == "winner" else self.loser.finishertype))
        self.edge = "winner"
        self.finisherStage()


    def finisherStage(self):
        finishLoop = True
        while finishLoop:
            if self.edge == "loser":
                self.reversalFinisher()
                time.sleep(1)
            else:
                record_list = self.data["finisher_scenarios"]["winner"][self.winner.finishertype]
                records = [record.format(winner=self.winner.name, loser=self.loser.name, winner_finisher=self.winner.finisher, loser_finisher=self.loser.finisher) for record in record_list]

                self.output(random.choice(records))
            if self.finisherKickout and random.randrange(100) < 20:
                self.failedPin("Finisher")
                self.finisherKickout = False
            else:
                finishLoop = False

        self.endMatch()
        finishLoop = False


    def endMatch(self):
        standardpin = self.data["standardpin"]
        standard_formatted = [record.format(winner=self.winner.name, loser=self.loser.name) for record in standardpin]
        surprisepin = self.data["surprisepin"]
        surprise_formatted = [record.format(winner=self.winner.name, loser=self.loser.name) for record in surprisepin]

        if self.edge == "loser":
            self.output(random.choice(surprise_formatted))
        else:
            self.output(random.choice(standard_formatted))

        alignment_responses = {
            range(80, 101): f"The crowd explodes!! {self.winner.name} celebrates with the crowd!",
            range(50, 80): f"{self.winner.name} is greeted by cheers and applause by the crowd!",
            range(20, 50): f"{self.winner.name} relishes in the groans heard in the crowd. They aren't happy with this win.",
            range(0, 20): f"Loud boos and jeers are heard from the fans. {self.winner.name} taunts them in celebration! He won't win them over that way."
        }

        for align_range, response in alignment_responses.items():
            if self.winner.align in align_range:
                self.output(response)
                break

    def recordsListEdgeStyle(self, dataList):
        record_list = self.data[dataList][self.edge][self.loser.style if self.edge == "loser" else self.winner.style]
        records = [record.format(winner=self.winner.name, loser=self.loser.name, winner_finisher=self.winner.finisher, loser_finisher=self.loser.finisher) for record in record_list]

        return random.choice(records)

    def recordsListEdgeFinisherType(self, dataList):
        record_list = self.data[dataList][self.edge][self.loser.finishertype if self.edge == "loser" else self.winner.finishertype]
        records = [record.format(winner=self.winner.name, loser=self.loser.name, winner_finisher=self.winner.finisher, loser_finisher=self.loser.finisher) for record in record_list]

        return random.choice(records)