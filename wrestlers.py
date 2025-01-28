class Wrestler:
    def __init__(self, name, height, weight, music, entrance, catchphrase, tauntstyle, hometown, overall, align, mic_skill, style, signature, signaturetype, finisher, finishertype):
        self.name = name
        self.height = height
        self.weight = weight
        self.music = music
        self.entrance = entrance
        self.catchphrase = catchphrase
        self.tauntstyle = tauntstyle
        self.hometown = hometown
        self.overall = overall
        self.mic_skill = mic_skill
        self.align = align
        self.style = style
        self.signature = signature
        self.signaturetype = signaturetype
        self.finisher = finisher
        self.finishertype = finishertype

    # Allows for a print(ObjectName) to give actual values
    def __str__(self):
        return f"{self.name} - {self.overall}"

    # Be careful not to call a function the same as one of the self init variables
    # The self variables are global within the class.
    # Called by 'Object.performFinisher()'
    def performFinisher(self):
        print(self.name + " drops the " + self.finisher + "!")

'''

Undertaker = Wrestler("The Undertaker", 88, "Tombstone Piledriver")

print(Undertaker.name)
print(Undertaker.overall)
print(Undertaker)
Undertaker.performFinisher()

print("----------------")


wrestlerary = [
    Wrestler("The Undertaker", 88, "Tombstone Piledriver"),
    Wrestler("The Rock", 87, "Rock Bottom"),
    Wrestler("Steve Austin", 92, "Stone Cold Stunner")
]
print(wrestlerary[2])


wrestledict = {
    "under": Wrestler("The Undertaker", 88, "Tombstone Piledriver"),
    "rock": Wrestler("The Rock", 87, "Rock Bottom"),
    "austin": Wrestler("Steve Austin", 92, "Stone Cold Stunner")
}
print("Wrestler Dictionary (Raw):", wrestledict)


print("Wrestler Dictionary Contents:")
for key, wrestler in wrestledict.items():
    print(f"{key}: {wrestler}")


print(wrestledict['rock'])
'''