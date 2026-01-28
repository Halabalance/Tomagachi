from tbaby import TomagachiBaby
from tchild import TomagachiChild
from tteen import TomagachiTeen
from tadult import TomagachiAdult

import time
from enum import Enum

class UserTomogachi:

    class Threshold(Enum):
        BABY = 5
        CHILD = 13
        TEEN = 18




    def __init__(self, user_name):
        self.HUNGER_INTERVAL  = 3600                                                     # decrease hunger every hour 3600
        self.ENERGY_INTERVAL = 7200                                                     # decrease happiness every 2 hours 7200
        self.HAPPINESS_INTERVAL = 7200                                                   # decrease happiness every 2 hours
        self.TIME_INTERVAL = 86400                                                       # increase age by 1 every 24 hours 86400

        self.last_recorded_happiness = time.time()
        self.last_recorded_hunger = time.time()
        self.last_recorded_energy = time.time()
        self.last_recorded_time = time.time()
        self.user_pet = TomagachiBaby(user_name, 100, 100, 100, 0, True,[])

    def evolve(self):
        if self.user_pet.alive:
            if isinstance(self.user_pet, TomagachiBaby):
                self.user_pet = TomagachiChild(self.user_pet.name, self.user_pet.hunger, self.user_pet.happiness,
                                               self.user_pet.energy,self.user_pet.age,
                                               self.user_pet.alive, self.user_pet.traits)

            elif isinstance(self.user_pet, TomagachiChild):
                self.user_pet = TomagachiTeen(self.user_pet.name, self.user_pet.hunger, self.user_pet.happiness,
                                               self.user_pet.energy,self.user_pet.age,
                                               self.user_pet.alive, self.user_pet.traits)

            elif isinstance(self.user_pet, TomagachiTeen):
                self.user_pet = TomagachiAdult(self.user_pet.name, self.user_pet.hunger, self.user_pet.happiness,
                                               self.user_pet.energy,self.user_pet.age,
                                               self.user_pet.alive, self.user_pet.traits)
            else:
                raise Exception("pet is adult: cant evolve further")
        else:
            raise Exception("pet not alive")


    def age(self):
        if time.time() - self.last_recorded_time < self.TIME_INTERVAL:
            return

        self.user_pet.increase_age()
        age = self.user_pet.age
        self.last_recorded_time = time.time()

        if isinstance(self.user_pet, TomagachiBaby) and age >= self.Threshold.BABY.value:
            self.evolve()
        elif isinstance(self.user_pet, TomagachiChild) and age >= self.Threshold.CHILD.value:
            self.evolve()
        elif isinstance(self.user_pet, TomagachiTeen) and age >= self.Threshold.TEEN.value:
            self.evolve()



    def adjust_hunger(self):
        self.user_pet.set_hunger(max(0, self.user_pet.hunger - self.user_pet.HUNGER_RATE))

    def adjust_happiness(self):
        self.user_pet.set_happiness(max(0, self.user_pet.happiness - self.user_pet.HAPPINESS_RATE))

    def adjust_energy(self):
        self.user_pet.set_energy(max(0, self.user_pet.energy - self.user_pet.ENERGY_RATE))


    def entropify(self):
        if time.time() - self.last_recorded_happiness > self.HAPPINESS_INTERVAL:
            self.adjust_happiness()
            self.last_recorded_happiness = time.time()

        if time.time() - self.last_recorded_hunger > self.HUNGER_INTERVAL:
            self.adjust_hunger()
            self.last_recorded_hunger = time.time()

        if time.time() -  self.last_recorded_energy > self.ENERGY_INTERVAL:
            self.adjust_energy()
            self.last_recorded_energy = time.time()







