import csv
import os

path = os.path.dirname(os.path.realpath(__file__)) # Getting the path of this python file.
path = path + "/data.csv" # Getting the path of the csv file relative to this python file.

f = open(path)
reader = csv.reader(f)
print(reader)

for cell in reader:
    id = cell[0]
    command = cell[1]
    position = cell[2]
    print("ID " + str(id) + " " + "command " + " " + str(command) + " " + "Pos " + str(position))
