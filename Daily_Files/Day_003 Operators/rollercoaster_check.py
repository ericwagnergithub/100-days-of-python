print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0 

if height >= 120:
    print("You can ride!")
    age = int(input("What is your age? "))
    if age < 12:
        print("Pay $5")
        bill = 5
    elif age >12 and age <= 18:
        print("Pay $7")
        bill = 7
    ## Mid-life crisis window
    elif age >= 45 and age <= 55:
        print("Everything will be ok. Have a free ride on us!")
    else:
        print("Pay $12")
        bill = 12

    wants_photo = input("Do you want a photo for $3? Y or N. ")
    if wants_photo == "Y":
        bill += 3
    print(f"Your final bill is ${bill}")

else:
    print("Sorry you are too short.")