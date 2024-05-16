print("Welcome to the tip calculator!")

bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people are splitting the bill? "))

##split_amount = round(bill * (1 + tip / 100) / people ,2))
split_amount = "{:.2f}".format(bill * (1 + tip / 100) / people)

print(f"Each persona should pay: ${split_amount}")