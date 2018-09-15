class BigInt():
    def __init__(self,num,node_size=1):
        #convert list of string into list of int
        self.list = list(map(int,num))

    def add(self, other):
        if isinstance(other, BigInt):
            return self.__add_bigint(other)
        else:
            raise ValueError('Cannot add BigInt and %s' % (BigInt))

    def multiply(self, other):
        if isinstance(other, BigInt):
            return self.__mul_bigint(other)
        else:
            raise ValueError('Cannot multiply BigInt and %s' % (BigInt))

    def __add_bigint(self, other):
        nodes1 = self.list
        nodes2 = other.list

        nodes1 = [0] * (len(nodes2) - len(nodes1)) + nodes1
        nodes2 = [0] * (len(nodes1) - len(nodes2)) + nodes2

        zipped = [pair for pair in zip(nodes1, nodes2)]
        added = [a + b for (a, b) in zipped]
        normalized = _nodes_normalize(added)

        self.list = normalized

        return self

    def __mul_bigint(self, other):
        nodes1 = self.list
        nodes2 = other.list

        # We multiply each node with a list of nodes.
        multiplied = [[a * b for b in nodes2] for a in nodes1]
        # We then pad extra 0s based on digit position
        padded = [a + [0] * (len(multiplied) - i)
                  for i, a in enumerate(multiplied, 1)]
        biginted = [BigInt(nodes) for nodes in padded]
        summed = reduce(lambda bigint, acc: acc.add(bigint), biginted)

        self.list = summed.list

        return self

    def __repr__(self):
        return ''.join(list(map(str,self.list)))


def _nodes_normalize(nodes, carry=0, acc=[]):
    if not nodes:
        if carry > 0:
            return [carry] + acc
        else:
            return acc
    else:
        num = nodes[-1] + carry
        new_num = num % 10
        new_carry = num // 10
        return _nodes_normalize(nodes[:-1], new_carry, [new_num] + acc)