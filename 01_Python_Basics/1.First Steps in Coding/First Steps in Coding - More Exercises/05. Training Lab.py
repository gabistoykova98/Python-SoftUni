import math
from math import floor
side_1 = float(input()) * 100
side_2 = float(input()) * 100

place_length = 120
place_width = 70
rows = math.floor(side_1 / place_length)
rows_2 = math.floor((side_2 - 100) / place_width)
workplaces = (rows * rows_2) - 3
print(workplaces)


