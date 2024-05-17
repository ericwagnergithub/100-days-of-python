line1 = ["⬜", "⬜", "⬜"]
line2 = ["⬜", "⬜", "⬜"]
line3 = ["⬜", "⬜", "⬜"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input("Where do you want to bury the treasure?")


# column = position[0]
# column_num=0
# if column == "A":
#     column_num = 0
# if column == "B":
#     column_num = 1
# if column == "C":
#     column_num = 2

# row = position[1]
# row_num = int(row)-1


letter = position[0].lower()
abc = ["a", "b", "c"]
column_num = abc.index(letter)
row_num = int(position[1])-1
print(column_num)


map[row_num][column_num] ="❌"
print(f"{line1}\n{line2}\n{line3}")