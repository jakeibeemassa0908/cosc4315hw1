class BigInt():
    def __init__(self,num,node_size=1):
        #convert list of string into list of int
        self.list = list(map(int,num))

    def add(self, other):
        if isinstance(other, BigInt):
            return self.__add_bigint(other)
        else:
            raise ValueError('Cannot add BigInt and %s' % (BigInt))

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

    def multiply(self,list2):
        sum_lists = []
        # diferentiate the longer list than the smaller list
        smallerList,longerList = (list2.list,self.list) if len(list2.list)<len(self.list) else (self.list,list2.list)

        multiplier = 0
        for i in reversed(range(len(smallerList))):
            new_list = []
            carry = 0
            for j in reversed(range(len(longerList))):
                numToAdd=(smallerList[i] * longerList[j])+ carry
                carry = numToAdd//10
                new_list.append(numToAdd%10)
            if carry > 0:
                new_list.append(carry)
            new_list.reverse()
            sum_lists.append(new_list+ [0] * multiplier)

            multiplier+=1
        self.list = sum_lists[0]

        for l in sum_lists[1:]:
            self.add(BigInt(l))

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