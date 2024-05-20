print("The Love Calculator is calculating your score...")
name1 = input("What is the first name?")
name2 = input("What is the second name?")

combined_names = name1 + name2
lower_names = combined_names.lower()

t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")
true = t + r + u + e

l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
love = l + o + v + e

score = str(true) + str(love)
score = int(score)

if score < 10 and score > 90:
    print(f"Your score is {score} and you go together like coke and mentos.")
elif score < 40 and score > 50:
    print(f"Your score is {score} and you are meh.")
else:
    print(f"Your score is {score}.")