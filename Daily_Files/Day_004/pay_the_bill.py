import random

names_input = input("Who is eating?")
names = names_input.split(", ")
random_num = random.randint(0,len(names)-1)
person_paying = names[random_num]
print(f"The person paying this time is {person_paying}.")