def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True 
            else:
                return False
        else:
            return True
    else:
        return False
  
# TODO: Add more code here 👇
def days_in_month(year_input, month_input):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
    days_output = 0
    if is_leap(year_input) and month_input == 2:
        return 29
    else:
        days_output = month_days[month_input-1]
        return days_output
  

  
#🚨 Do NOT change any of the code below 
year = int(input()) # Enter a year
month = int(input()) # Enter a month
days = days_in_month(year, month)
print(days)

