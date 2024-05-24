import math

def paint_calc(height, width, cover):
    num_cans = math.ceil(height*width/cover)
    print(f"You'll need {num_cans} cans of paint.")



test_h = int(input()) #Height of wall (m)
test_w = int(input()) # Width of wall (m)
coverage = 5 # sq ft per can coverage


paint_calc(height=test_h, width = test_w, cover = coverage)