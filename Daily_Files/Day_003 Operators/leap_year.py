year = int(input("What year are you checking? "))

if year % 4 == 0: 
    if year % 100 != 0:
        if year % 400 == 0:
            print("Leap Year!")
        else:
            print("Not a leap year :(")
    else:
        print("Leap year")
else:
    print("Not a leap year :(")