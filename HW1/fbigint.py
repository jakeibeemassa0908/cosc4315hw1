"""A set of functions for working with bigints.
"""


def add(bigint1, bigint2):
    nodes1 = bigint1[2]
    nodes2 = bigint2[2]
    new_nodesize = bigint1[1]

    nodes1 += [0] * (len(nodes2) - len(nodes1))
    nodes2 += [0] * (len(nodes1) - len(nodes2))

    added = [a + b for a, b in zip(nodes1, nodes2)]
    normalized = __nodes_normalize(added, new_nodesize)

    return new(new_nodesize, normalized)


def __nodes_normalize(nodes, nodesize, carry=0, acc=[]):
    if not nodes:
        if carry > 0:
            return __nodes_normalize([carry], nodesize, 0, acc)
        else:
            return acc
    else:
        num, rest = nodes[0], nodes[1:]
        total = num + carry
        new_num = total % (10 ** nodesize)
        new_carry = total // (10 ** nodesize)
        return __nodes_normalize(rest, nodesize, new_carry, acc + [new_num])


def isbigint(value):
    return isinstance(value, tuple) and len(value) == 3 and value[0] == 'bigint'


def new(nodesize, nodes):
    return ('bigint', nodesize, nodes)
