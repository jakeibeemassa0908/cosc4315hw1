import os
from BigInt import BigInt
"""
Without recursion
"""
def infinitearithmetic():
    path = os.path.join(os.path.dirname(__file__),"input.txt")
    with open(path)as f:
        lines = f.readlines()

    for line in lines:
        line = line.strip()
        if '*' in line:
            values = line.split("*")
            product = int(values[0])* int(values[1])
            print(line.rstrip('\n')+ ' = '+ str(product))

        elif '+' in line:
            values = line.split('+')
            x = BigInt(values[0])
            y = BigInt(values[1])
            x.add(y)
            print(line.rstrip('\n') + ' = '+ str(x))


infinitearithmetic()