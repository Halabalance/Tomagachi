
class TomagachiBase:
    def __init__(self,name:str, hunger:int, happiness:int, energy:int, age:int,alive:bool,hunger_rate:int, happiness_rate:int, energy_rate:int, traits:list):
        self.name = name
        self.hunger = hunger
        self.happiness = happiness
        self.energy = energy
        self.age = age
        self.alive = alive
        self.traits = traits
        self.HUNGER_RATE = hunger_rate
        self.HAPPINESS_RATE = happiness_rate
        self.ENERGY_RATE = energy_rate



    def set_hunger(self, value: int):
        if value > 100:
            self.hunger = 100
        else:
            if value == 0:
                self.die()
            else:
                self.hunger = value


    def set_happiness(self, value: int):
        if value > 100:
            self.happiness = 100
        elif value == 0:
            self.die()
        else:
            self.happiness = value

    def set_energy(self, value: int):
        if value > 100:
            self.energy = 100
        elif value == 0:
            self.die()
        else:
            self.energy = value

    def increase_age(self):
        self.age += 1

    def die(self):
        self.alive = False

    #to be overwritten
    def speak(self):
        pass


