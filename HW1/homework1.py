import os

"""
Without recursion
"""
def infinitearithmetic():
    path = os.path.join(os.path.dirname(__file__),"input.txt")
    with open(path)as f:
        lines = f.readlines()

    for line in lines:
        if '*' in line:
            values = line.split("*")
            product = int(values[0])* int(values[1])
            print(line.rstrip('\n')+ ' = '+ str(product))

        elif '+' in line:
            values = line.split('+')
            add = int(values[0])+ int(values[1])
            print(line.rstrip('\n') + ' = '+ str(add))


infinitearithmetic()