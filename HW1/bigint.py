class BigInt():
    def __init__(self, **kwargs):
        self.nodes = kwargs.get('nodes', [0])
        self.node_size = kwargs.get('node_size', 1)

    def __add__(self, other):
        if isinstance(other, BigInt):
            return self.__add_bigint(other)
        elif isinstance(other, int):
            return self + BigInt.fromint(other)
        else:
            raise ValueError('Cannot add BigInt and %s' % (other.__class__.__name__))

    def __mul__(self, other):
        if isinstance(other, BigInt):
            return self.__mul_bigint(other)
        else:
            raise ValueError('Cannot multiply BigInt and %s' % (other.__class__.__name__))

    def __radd__(self, other):
        return self + other

    @classmethod
    def parse(cls, string, digits_per_node=1):
        try:
            nodes = [int(d) for d in string]
            return BigInt(nodes=nodes, node_size=digits_per_node)
        except:
            raise ValueError('`string` is not a parseable BigInt.')

    @classmethod
    def fromint(cls, integer, digits_per_node=1):
        return cls.parse(str(integer), digits_per_node)

    def __add_bigint(self, other):
        nodes1 = self.nodes
        nodes2 = other.nodes

        nodes1 = [0] * (len(nodes2) - len(nodes1)) + nodes1
        nodes2 = [0] * (len(nodes1) - len(nodes2)) + nodes2

        zipped = [pair for pair in zip(nodes1, nodes2)]
        added = [a + b for (a, b) in zipped]
        normalized = _nodes_normalize(added)

        return BigInt(nodes=normalized, node_size=self.node_size)

    def __mul_bigint(self, other):
        nodes1 = self.nodes
        nodes2 = other.nodes

        # We multiply each node with a list of nodes.
        multiplied = [[a * b for b in nodes2] for a in nodes1]
        # We then pad extra 0s based on digit position
        padded = [a + [0] * (len(multiplied) - i)
                  for i, a in enumerate(multiplied, 1)]
        biginted = [BigInt(nodes=nodes, node_size=self.node_size) for nodes in padded]
        summed = sum(biginted)

        return summed

    def __repr__(self):
        if not self.nodes:
            return '0'
        else:
            return ''.join(str(node) for node in self.nodes)


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
