target = int(input())
sum = 0
if target <= 1000:
    for number in range(2, target + 1 ,2):
        sum += number

print(f"The sum is {sum}.")
