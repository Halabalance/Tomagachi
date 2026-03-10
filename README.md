
  _____                                                    _____
 ( ___ )                                                  ( ___ )
  |   |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|   |
  |   |    ░█░█░█▀█░█░░░█▀█░█▀▄░█▀█░█░░░█▀█░█▀█░█▀▀░█▀▀    |   |
  |   |    ░█▀█░█▀█░█░░░█▀█░█▀▄░█▀█░█░░░█▀█░█░█░█░░░█▀▀    |   |
  |   |    ░▀░▀░▀░▀░▀▀▀░▀░▀░▀▀░░▀░▀░▀▀▀░▀░▀░▀░▀░▀▀▀░▀▀▀    |   |
  |___|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|___|
 (_____)                                                  (_____)

# Tamagotchi
 A retro-styled virtual pet simulator, Raise your Tamagotchi from a baby to an adult while managing their hunger,
happiness, and energy levels.

## Table of Contents:
- [Features](#features)
- [Installation](#installation)
- [Game Mechanics](#game-mechanics)
- [Technical Details](#technical-details)

# Features
- Complete hunger, energy and happiness system designed using real world time
- Full graphical user interface to see your pet
- Autosaves to data.dat whenever you close the app
- pet can talk using random words
- cooldown after feeding, playing or taking the pet to sleep

# Installation
1) download python using https://www.python.org/
2) download all .py files and put them in any folder
3) run maingui.py

# Game mechanics
There are main 4 main stages your pet will go through

```
    🐣  ------>  🐤  ------>  🐔  ------>  🦅
   Baby        Child         Teen         Adult
 
```
Each pet level has its own different rates of hunger, energy, and happiness, for example, a child will get hungrier than an adult

|                | Baby | Child | Teen | Adult |
|----------------|------|-------|------|-------|
| Hunger rate    | 10   | 25    | 25   | 15    |
| Happiness rate | 15   | 10    | 25   | 15    |
| Energy rate    | 20   | 15    | 30   | 25    |

at each stage, the pet will evolve into its next stage at a certain age

|               | Baby | Child | Teen |
|---------------|------|-------|------|
| Evolve at age | 5    | 13    | 18   |

dont worry, the game isnt ultra realistic.
1 year in game is equal to 24 hours in real life.

## List of quips you can get at each stage
In game, you can get multiple possible words or quips from your pet
### Baby

- "Goo goo gaga!"
- "Ba-ba-ba-ba-BA!"
- "Pffffftttttt!"
- "Ma... ma... ma... MOO!"
- "Dada? Dada!"
- "Agloo gleep glub."
- "WaAaAaAaAaH!"
- "Yum-yum-yum-yum!"
- "Buh... buh... ball!"
- "Eeeeeeeeeee!"
- "Gah! Gah! Blah!"
- "Mmmmmm-ba!"
- "Zzzzzzz... *snort*"
- "Oooooh? Aaaaah!"
- "Lululululu!"
- "Daba dwee bop!"
- "Geh... geh... dee.. dee.. dee"
- "Squeak!"
- "Ababa-daba-doo?"
- "Blub-blub-blub."
- "awawawawaw aaaaaa"
- "AAAAAAAAAAaaaaaa"
- "gwh gaaa aaa"
- "WAHHHHHHHH WAHHHHHHHHH!!!!"

### Child
- "Hello!","Hi!", "I want to be an astronaut!", "I love worms!", "I hate broccoli!","What are you?",
- "Are you my parent?", "I want candy!", "Why is the sky blue?",
- "How do birds sleep without falling off trees?","Do fish get thirsty?",
- "Can we go to the moon tomorrow?",
- "Is a hot dog a sandwich?",
- "I found a cool rock! Can I keep it in my bed?",
- "How many days until my birthday?",
- "If I grow up, do I have to stop playing?",
- "I can't clean my room because my legs are tired.",
- "Can I have a bowl of ketchup?",
- "Do cows drink milk or water?",
- "I found a rock that looks like a potato!",
- "Why do I have ten toes but only one head?",
- "Can we have breakfast for dinner?",
- "I can run faster if I wear my dinosaur shoes!",
- "Is it tomorrow yet?",
- "Look! I can whistle with my nose!",
- "How many stars are in the sky? Let’s count them!",
- "I’m going to build a robot that cleans my room.",
- "I have a secret, but I forgot what it is.",
- "Can dogs talk in their sleep?",
- "Why do grown-ups drink 'bean water' in the morning?",
- "I want to be a dinosaur when I grow up!",
- "Can I keep this ladybug as a pet?",
- "Do you have games on your phone?",
- "I hate math!",
- "Do you have a car?"
- "Look at this booger i pulled out!"
### Teen
- What do you want?
- Leave me alone!
- Go away!!!
- Im busy!
- What now?!
- I hate you!
- Whatever.
- I'm literally so bored right now.
- Can you not?
- ughhhhhhhhhhh
- UGHHHHHHHHHH
- Did I ask?
- Dont you have anything better to do?
- Great, you again...
- snoring
- wha?
- huh?
- WHAT??
- Whats up?
- hey
- Oh, i didn't hear you i had my AirPods in.
- uhhhhhhh
- Before you say it, i dont care.
- Coughing
- Ok.
### Adult
- "Hello!",
- "Nice to see you again!",
- "Is that tax-deductible?",
- "Do you accept credit card?",
- "Is that gluten free?",
- "How is your 401k looking these days?",
- "We need to clean the gutters before winter hits.",
- "Is there a draft in here? Close the window.",
- "Did you lock the front door? Check it again.",
- "I hurt my back sleeping.",
- "We really need to watch our cholesterol.",
- "I’m excited about my new vacuum cleaner.",
- "I love a good Tupperware that seals properly.",
- "Look at the gas prices!",
- "I need to schedule a dentist appointment.",
- "Does this noise sound expensive to you?",
- "I can't believe it's already night.",
- "Do you think we have enough Tupperware for leftovers?",
- "Gas went up ten cents since yesterday. Unbelievable.",
- "It’s not the heat that gets you, it’s the humidity.",
- "I got a really good rate on my car insurance.",
- "don’t slam the door.",
- "This vacuum cleaner has excellent suction.",
- "The new generation has it so easy",
- "I used to have to memorize everyone's phone number.",
- "They wouldn't last a day without Wi-Fi.",
- "We used to play outside until the streetlights came on.",
- "I hate my wife",
- "They spend more time taking pictures of their food than eating it.",
- "Why are we buying bottled water when the tap works perfectly fine?",
- "I don't care if the shoes have holes in them; you can't see them from a distance.",
- "She left the porch light on all night. That’s basically like burning a dollar bill in the driveway.",
- "We aren't getting the 'extended warranty.' That's how they get you.",
- "I’m not 'cheap,' I’m 'fiscally responsible.' There’s a difference.",
- "Do we really need a Netflix subscription AND the internet? It feels redundant.",
- "I’ve been using this same razor blade since Thanksgiving and it’s still got plenty of life.",
- "I told her the 'Check Engine' light is just a suggestion to keep the mechanics in business."
- "Oh noooooo please dont take the kids... what will i ever do?!"
- "Im sleeping on the couch tonight..."

## Game Over

Your Tamagotchi dies if any stat reaches 0:

When this happens:
- You'll see a death screen
- A message shows how long they lived
- Game saves the final state
- Start over with a new pet

# Technical Details

### Architecture

**Object-Oriented Design:**
```
TomagachiBase (abstract)
    ├── TomagachiBaby
    ├── TomagachiChild
    ├── TomagachiTeen
    └── TomagachiAdult

UserTomogachi (behavior controller)
    └── manages lifecycle & state transitions
```

**Threading Model:**
- Main thread: GUI rendering & user input
- Background thread: Stat decay & aging calculations
- Thread-safe operations with daemon threads

### Time Intervals

```python
HUNGER_INTERVAL = 3600      # 1 hour
ENERGY_INTERVAL = 7200      # 2 hours
HAPPINESS_INTERVAL = 7200   # 2 hours
TIME_INTERVAL = 86400       # 24 hours (1 day)
```

### Stat Decay Rates

| Stage | Hunger Rate | Happiness Rate | Energy Rate |
|-------|-------------|----------------|-------------|
| Baby  | 10/hour     | 15/2hrs        | 20/2hrs     |
| Child | 25/hour     | 15/2hrs        | 15/2hrs     |
| Teen  | 25/hour     | 25/2hrs        | 30/2hrs     |
| Adult | 15/hour     | 15/2hrs        | 25/2hrs     |

### Save System

Uses Python's `pickle` module to serialize:
- Current pet state (all stats)
- Life stage
- Age
- Alive/dead status
- Trait list
- Last recorded timestamps

**Save file location:** `save.dat` in game directory
