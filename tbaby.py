from tbase import TomagachiBase
import random


class TomagachiBaby(TomagachiBase):


    def __init__(self, name: str, hunger: int, happiness: int, energy: int, age: int, alive: bool, traits: list):
        super().__init__(name, hunger, happiness, energy, age, alive, 10, 15, 20, traits)

        self.quips = [
            "Goo goo gaga!","Ba-ba-ba-ba-BA!","Pffffftttttt!","Ma... ma... ma... MOO!","Dada? Dada!","Agloo gleep glub.",
            "WaAaAaAaAaH!","Yum-yum-yum-yum!","Buh... buh... ball!","Eeeeeeeeeee!","Gah! Gah! Blah!",
            "Mmmmmm-ba!",
            "Zzzzzzz... *snort*",
            "Oooooh? Aaaaah!",
            "Lululululu!",
            "Daba dwee bop!",
            "Geh... geh... dee.. dee.. dee",
            "Squeak!",
            "Ababa-daba-doo?",
            "Blub-blub-blub.",
            "awawawawaw aaaaaa"
            "AAAAAAAAAAaaaaaa"
            "gwh gaaa aaa"
            "WAHHHHHHHH WAHHHHHHHHH!!!!"
        ]

    def speak(self):
        print(random.choice(self.quips))


    def __str__(self):
        return "Baby"