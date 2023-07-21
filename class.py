import csv

class csv_class():
    @classmethod
    def reader(cls):
        with open('data.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
            print(items)
            print("____________")
        
        for item in items:
            print(item)
            print(item.get('name'))
            print(item.get('price'))
            print(item.get('quantity'))


csv_class.reader()


# //////////////////////////////////////////////////////////////////////////////////////////
# second method:

# import os
# path = os.path.dirname(os.path.realpath(__file__))
# path = path + "/routines/routine.csv"

# f = open(path)
# reader = csv.reader(f)
# print(reader)


# for cell in reader:
#     id = cell[0]
#     command = cell[1]
#     position = cell[2]
#     delay = cell[3]
#     print("ID " + str(id) + " " + "command " + " " + str(command) + " " + "Pos " + str(position) + " " + "Delay " + str(delay))