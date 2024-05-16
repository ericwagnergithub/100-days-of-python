print("Thank you for choosing Python Pizza Deliveries!")
bill = 0

size = input("What size pizza do you want? S, M, or L. ")
if size == "S":
    bill = 15
if size == "M":
    bill = 20
if size == "L":
    bill = 25

add_pepperoni = input("Would you like pepperoni? $ 2 for S. $3 for M/L. Y or N. ")
if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    if size == "M" or size == "L":
        bill += 3

if add_pepperoni == "N":    
    bill = bill 

extra_cheese = input("Would you like extra cheese for $1? Y or N. ")
if extra_cheese == "Y":
    bill += 1

if extra_cheese == "N":    
    bill = bill 

print(f"Your final bill is ${bill}.")