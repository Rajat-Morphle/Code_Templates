import os
import csv

path = os.path.dirname(os.path.realpath(__file__))
path = path + "/routines/routine.csv"

f = open(path)
reader = csv.reader(f)
# print(reader)

for cell in reader:
    id = cell[0]
    command = cell[1]
    position = cell[2]
    delay = cell[3]
    print("ID: " + str(id) + " | " + "command: " + str(command) + " | " + "Pos: " + str(position) + " | " + "Delay: " + str(delay))