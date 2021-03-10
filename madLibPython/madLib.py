import random
for x in range(3):
    decider = random.randint(1, 3)
print("Welcome to this Mad Lib game!")
if decider == 1:
    adjective = input("Insert an adjective: ")
    animal = input("Insert an animal: ")
    food = input("Insert a food: ")
    adjective2 = input("Insert another adjective: ")
    madLib = f"Yesterday was a {adjective} day. So much happened. In the morning I saw a {adjective2} {animal} it was eating {food}"
    print(madLib)
elif decider == 2:
    animal = input("Insert an animal: ")
    adjective = input("Insert an adjective: ")
    object = input("Insert an object: ")
    color = input("Insert a color: ")
    adjective2 = input("Insert another adjective: ")
    animal2 = input("Insert another animal: ")
    madLib = f"When I went to the store the other day it was {adjective} some little {animal}s were running around and nobody cared! When I went to get some {object}s they were all out until a {adjective2} man came with a {color} cane that had a {animal2} head on top of it and handed the {object} to me for no cost"
    print(madLib)
elif decider == 3:
    month = input("Insert a month: ")
    food3 = input("Insert a plural food: ")
    country = input("Insert a country: ")
    food = input("Insert another plural food: ")
    food2 = input("Insert another plural food: ")
    foodTogether = f"{food} with {food2} on top of it"
    madLib = f"Last {month} I went on a trip to {country}. While I was there we went to a local sit down place and it had completely different food! The first thing on the menu was {food} with {food2} on top of it! The next dish was {food3} but instead of being cooked they served it raw. I picked the third option which was french fries because {foodTogether} and raw {food3} seemed really gross." 
    print(madLib)
else:
    print("There has been an error")
