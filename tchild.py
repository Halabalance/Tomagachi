from tbase import TomagachiBase
import random


class TomagachiChild(TomagachiBase):


    def __init__(self, name: str, hunger: float, happiness: float, energy: float, age: int, alive: bool, traits: list):
        super().__init__(name, hunger, happiness, energy, age, alive, 25, 15, 15, traits)

        self.quips = [
            "Hello!","Hi!", "I want to be an astronaut!", "I love worms!", "I hate broccoli!","What are you?",
            "Are you my parent?", "I want candy!", "Why is the sky blue?",
            "How do birds sleep without falling off trees?","Do fish get thirsty?",
            "Can we go to the moon tomorrow?",
            "Is a hot dog a sandwich?",
            "I found a cool rock! Can I keep it in my bed?",
            "How many days until my birthday?",
            "If I grow up, do I have to stop playing?",
            "I can't clean my room because my legs are tired.",
            "Can I have a bowl of ketchup?",
            "Do cows drink milk or water?",
            "I found a rock that looks like a potato!",
            "Why do I have ten toes but only one head?",
            "Can we have breakfast for dinner?",
            "I can run faster if I wear my dinosaur shoes!",
            "Is it tomorrow yet?",
            "Look! I can whistle with my nose!",
            "How many stars are in the sky? Let’s count them!",
            "I’m going to build a robot that cleans my room.",
            "I have a secret, but I forgot what it is.",
            "Can dogs talk in their sleep?",
            "Why do grown-ups drink 'bean water' in the morning?",
            "I want to be a dinosaur when I grow up!",
            "Can I keep this ladybug as a pet?",
            "Do you have games on your phone?",
            "I hate math!",
            "Do you have a car?"
            "Look at this booger i pulled out!"
        ]

    def speak(self):
        print(random.choice(self.quips))

    def __str__(self):
        return "Child"