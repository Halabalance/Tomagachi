from tbase import TomagachiBase
import random


class TomagachiTeen(TomagachiBase):


    def __init__(self, name: str, hunger: int, happiness: int, energy: int, age: int, alive: bool, traits: list):
        super().__init__(name, hunger, happiness, energy, age, alive, 25, 25, 30, traits)

        self.quips = [
            "What do you want?",
            "Leave me alone!"
            "Go away!!!"
            "I fucking HATE you!"
            "Im busy!",
            "What now?!",
            "I hate you!",
            "Fuck you",
            "Whatever.",
            "I'm literally so bored right now.",
            "Can you not?",
            "ughhhhhhhhhhh",
            "UGHHHHHHHHHH",
            "Did I ask?",
            "Dont you have anything better to do?",
            "Great, you again...",
            "*snoring*"
            "wha?",
            "huh?",
            "WHAT??",
            "Whats up?",
            "hey",
            "Oh, i didn't hear you i had my AirPods in.",
            "uhhhhhhh",
            "Before you say it, i dont care.",
            "*Coughing*",
            "Ok."
        ]

    def speak(self):
        print(random.choice(self.quips))

    def __str__(self):
        return "Teen"