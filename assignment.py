import random
import math

ability_list = ['Strength', 'Dexterity', 'Constitution', 'Intelligence', 'Wisdom', 'Charisma']
proficiency_list = [
    ['Athletics'],
    ['Acrobatics', 'Slieght of Hand', 'Stealth'],
    [],
    ['Arcana', 'History', 'Investigation', 'Nature', 'Religion'],
    ['Animal Handling', 'Insight', 'Medicine', 'Perception', 'Survival'],
    ['Deception', 'Intimidation', 'Performance', 'Persuasion']
]
proficiency_list_ref = []
flat_proficiency_list = []
for sublist in proficiency_list:
    for element in sublist:
        proficiency_list_ref.append(element)
        flat_proficiency_list.append([element, ability_list[proficiency_list.index(sublist)]])
flat_proficiency_list.sort()
proficiency_list_ref.sort()
race_and_stats = [
    ['Dragonborn', [2, 0, 0, 0, 0, 1]],
    ['Dwarf', [0, 0, 2, 0, 0, 0]],
    ['Elf', [0, 2, 0, 0, 0, 0]],
    ['Gnome', [0, 0, 0, 2, 0, 0]],
    ['Half-Elf', [0, 0, 0, 0, 0, 2]], #Plus 1 to 2 other scores
    ['Halfling', [0, 2, 0, 0, 0, 0]],
    ['Half-Orc', [2, 0, 1, 0, 0, 0]],
    ['Human', [1, 1, 1, 1, 1, 1]],
    ['Tiefling', [0, 0, 0, 1, 0, 2]]
]
#Class, hp, saves, #pros, and pro-list
class_bonus = [
    ['Barbarian', 12, ['Strength', 'Constitution'], 2,
        ['Animal Handling', 'Athletics', 'Intimidation', 'Nature',
         'Perception', 'Survival']],
    ['Bard', 8, ['Dexterity', 'Charisma'], 3,
        ['Athletics', 'Acrobatics', 'Slieght of Hand', 'Stealth',
         'Arcana', 'History', 'Investigation', 'Nature', 'Religion',
         'Animal Handling', 'Insight', 'Medicine', 'Perception', 'Survival',
         'Deception', 'Intimidation', 'Performance', 'Persuasion']],
    ['Cleric', 8, ['Wisdom', 'Charisma'], 2,
        ['History', 'Insight', 'Medicine', 'Persuasion', 'Religion']],
    ['Druid', 8, ['Intelligence', 'Wisdom'], 2,
        ['Arcana', 'Animal Handling', 'Insight', 'Medicine', 'Nature',
         'Perception', 'Religion', 'Survival']],
    ['Fighter', 10, ['Strength', 'Constitution'], 2,
        ['Acrobatics', 'Animal Handling', 'Athletics', 'History',
         'Insight', 'Intimidation', 'Perception', 'Survival']],
    ['Monk', 8, ['Dexterity', 'Wisdom'], 2,
        ['Acrobatics', 'Athletics', 'History', 'Insight',
         'Religion', 'Stealth']],
    ['Paladin', 10, ['Wisdom', 'Charisma'], 2,
        ['Athletics', 'Insight', 'Intimidation', 'Medicine',
         'Persuasion', 'Religion']],
    ['Ranger', 10, ['Dexterity', 'Wisdom'], 3,
        ['Animal Handling', 'Athletics', 'Insight', 'Investigation',
         'Nature', 'Perception', 'Stealth', 'Survival']],
    ['Rogue', 8, ['Dexterity', 'Intelligence'], 4,
        ['Acrobatics', 'Athletics', 'Deception', 'Insight', 'Intimidation',
         'Investigation', 'Perception', 'Performance', 'Persuasion',
         'Sleight of Hand', 'Stealth']],
    ['Sorcerer', 6, ['Constitution', 'Charisma'], 2,
        ['Arcana', 'Deception', 'Insight', 'Intimidation', 'Persuasion',
         'Religion']],
    ['Warlock', 8, ['Wisdom', 'Charisma'], 2,
        ['Arcana', 'Deception', 'History', 'Intimidation', 'Investigation',
         'Nature', 'Religion']],
    ['Wizard', 6, ['Intelligence', 'Wisdom'], 2,
        ['Arcana', 'History', 'Insight', 'Investigation', 'Medicine',
         'Religion']]
]
#Intro
print("D&D Character Creation")
#Pick a class
print("Pick a class from the following.")
class_list = []
for option in class_bonus:
    class_list.append(option[0])
while True:
    print(class_list)
    my_class = input(">")
    if my_class in class_list:
        print(f"You have chosen to play as a {my_class}.")
        break
    else:
        print(f"Sorry, '{my_class}' isn't a class option.")
        print("Please select one of the following.")
#Pick a race
print("Pick a race from the following.")
race_list = []
for race in race_and_stats:
    race_list.append(race[0])
while True:
    print(race_list)
    my_race = input(">")
    if my_race in race_list:
        print(f"You have chosen to play as a {my_race}.")
        break
    else:
        print(f"Sorry, '{my_race}' isn't a race option.")
        print("Please select one of the following.")
#Half-elf clause
if my_race == "Half-Elf":
    print("Half-Elfs receive a +2 to charisma and a +1 to two other stats.")
    half_elf_choices = ['Strength', 'Dexterity', 'Constitution', 'Intelligence', 'Wisdom']
    while len(half_elf_choices) > 3:
        print("Select one of the following stats to increase.")
        print(half_elf_choices)
        stat_choice = input(">")
        if stat_choice in half_elf_choices:
            race_and_stats[4][1][ability_list.index(stat_choice)] = 1
            half_elf_choices.pop(half_elf_choices.index(stat_choice))
        else:
            print(f"Sorry, {stat_choice} is not an option.")
#Roll stats
my_rolls = []
modifiers = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth']
for i in range(6):
    low_roll = 6
    sum = 0
    for j in range(4):
        roll = random.randint(1, 6)
        sum += roll
        if roll < low_roll:
            low_roll = roll
    my_rolls.append(sum - low_roll)
my_rolls.sort(reverse=True)
#Pick stats
stat_list = ['Strength', 'Dexterity', 'Constitution', 'Intelligence', 'Wisdom', 'Charisma']
my_stats = race_and_stats[race_list.index(my_race)][1]
for i in range(6):
    while True:
        print("**********")
        print(f"Your {modifiers[i]} highest stat roll is {my_rolls[i]}.")
        print("Please choose a stat from the following to place your score.")
        print(stat_list)
        my_choice = input(">")
        if my_choice in stat_list:
            my_stats[ability_list.index(my_choice)] += my_rolls[i]
            stat_list.pop(stat_list.index(my_choice))
            break
        else:
            print(f"{my_choice}, is an invalid choice.")
#Add modifiers
my_mods = []
for stat in my_stats:
    my_mods.append(math.floor((stat - 10) / 2))
#Add saving throws
my_saving_throws = []
for mod in my_mods:
    my_saving_throws.append(mod)
for i in class_bonus[class_list.index(my_class)][2]:
    my_saving_throws[ability_list.index(i)] += 2
#Pick pros
for element in flat_proficiency_list:
    element[1] = my_mods[ability_list.index(element[1])]
print(f"As a {my_class} you can choose {class_bonus[class_list.index(my_class)][3]} proficiencies.")
for i in range(class_bonus[class_list.index(my_class)][3]):
    while True:
        print("**********")
        print(f"Choose your {modifiers[i]} proficiency from the following list:")
        print(class_bonus[class_list.index(my_class)][4])
        my_prof_choice = input(">")
        if my_prof_choice in class_bonus[class_list.index(my_class)][4]:
            class_bonus[class_list.index(my_class)][4].pop(class_bonus[class_list.index(my_class)][4].index(my_prof_choice))
            flat_proficiency_list[proficiency_list_ref.index(my_prof_choice)][1] += 2
            break
        else:
            print(f"Sorry, {my_prof_choice} is not an option.")
#Display info
print("**********")
print(f"Class: {my_class}")
print(f"Race: {my_race}")
print("**********")
print(f"HP: {class_bonus[class_list.index(my_class)][1] + my_mods[2]}")
print(f"Hit Die: d{class_bonus[class_list.index(my_class)][1]}")
print("**********")
print("Saving throws")
for i in range(6):
    print(f"{ability_list[i]}: +{my_saving_throws[i]}")
print("**********")
print("Abilities and modifiers")
for i in range(6):
    print("*****")
    print(f"{ability_list[i]}")
    print(f"Score: {my_stats[i]}")
    print(f"Modifier: +{my_mods[i]}")
print("**********")
print("Proficiencies")
for prof in flat_proficiency_list:
    print(f"{prof[0]}: +{prof[1]}")