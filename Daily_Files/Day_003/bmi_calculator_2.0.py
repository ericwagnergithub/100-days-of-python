#BMI Calculator
height = float(input("What is your height? "))
weight = int(input("What is your weight? "))
bmi = round(weight / height ** 2 , 2)
##print(int(bmi))

if bmi < 18.5:
    print(f"Your BMI is {bmi}. You are underweight")
elif bmi >= 18.5 and bmi <25:
    print(f"Your BMI is {bmi}. You have a normal weight")
elif bmi >= 25 and bmi <30:
    print(f"Your BMI is {bmi}. You are slightly overweight")
elif bmi >= 30 and bmi <35:
    print(f"Your BMI is {bmi}. ou are obese")
else:
    print(f"Your BMI is {bmi}. You are clinically obese")