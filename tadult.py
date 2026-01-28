from tbase import TomagachiBase
import random



class TomagachiAdult(TomagachiBase):


    def __init__(self, name: str, hunger: int, happiness: int, energy: int, age: int, alive: bool, traits: list):
        super().__init__(name, hunger, happiness, energy, age, alive, 15, 15, 25, traits)

        self.quips = [
            "Hello!",
            "Nice to see you again!",
            "Is that tax-deductible?",
            "Do you accept credit card?",
            "Is that gluten free?",
            "How is your 401k looking these days?",
            "We need to clean the gutters before winter hits.",
            "Is there a draft in here? Close the window.",
            "Did you lock the front door? Check it again.",
            "I hurt my back sleeping.",
            "We really need to watch our cholesterol.",
            "I’m excited about my new vacuum cleaner.",
            "I love a good Tupperware that seals properly.",
            "Look at the gas prices!",
            "I need to schedule a dentist appointment.",
            "Does this noise sound expensive to you?",
            "I can't believe it's already night.",
            "Do you think we have enough Tupperware for leftovers?",
            "Gas went up ten cents since yesterday. Unbelievable.",
            "It’s not the heat that gets you, it’s the humidity.",
            "I got a really good rate on my car insurance.",
            "don’t slam the door.",
            "This vacuum cleaner has excellent suction.",
            "The new generation has it so easy",
            "I used to have to memorize everyone's phone number.",
            "They wouldn't last a day without Wi-Fi.",
            "We used to play outside until the streetlights came on.",
            "I hate my wife",
            "They spend more time taking pictures of their food than eating it.",
            "Why are we buying bottled water when the tap works perfectly fine?",
            "I don't care if the shoes have holes in them; you can't see them from a distance.",
            "She left the porch light on all night. That’s basically like burning a dollar bill in the driveway.",
            "We aren't getting the 'extended warranty.' That's how they get you.",
            "I’m not 'cheap,' I’m 'fiscally responsible.' There’s a difference.",
            "Do we really need a Netflix subscription AND the internet? It feels redundant.",
            "I’ve been using this same razor blade since Thanksgiving and it’s still got plenty of life.",
            "I told her the 'Check Engine' light is just a suggestion to keep the mechanics in business."
            "Oh noooooo please dont take the kids... what will i ever do?!"
            "Im sleeping on the couch tonight..."
        ]

    def speak(self):
        print(random.choice(self.quips))

    def __str__(self):
        return "Adult"