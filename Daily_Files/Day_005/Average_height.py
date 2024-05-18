student_heights = input().split()
for n in range(0,len(student_heights)):
    student_heights[n] = int(student_heights[n])

total_height = 0
for height in student_heights:
    total_height += student_heights[n]

total_students = 0
for student in student_heights:
    total_students += 1

average_height = int(total_height/total_students)

print(f"Total Height = {total_height}")
print(f"Total Students = {total_students}")
print(f"Average Height = {average_height}")