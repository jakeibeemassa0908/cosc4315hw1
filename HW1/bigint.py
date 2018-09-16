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
            raise ValueError('Cannot add BigInt and %s' %
                             (other.__class__.__name__))

    def __mul__(self, other):
        if isinstance(other, BigInt):
            return self.__mul_bigint(other)
        else:
            raise ValueError('Cannot multiply BigInt and %s' %
                             (other.__class__.__name__))

    def __radd__(self, other):
        return self + other

    @classmethod
    def parse(cls, string, digits_per_node=1):
        try:
            chunked = _chunk_digits(string, digits_per_node)
            nodes = [int(node) for node in chunked]
            normalized = _nodes_normalize(nodes, digits_per_node)
            return BigInt(nodes=normalized, node_size=digits_per_node)
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
        normalized = _nodes_normalize(added, self.node_size)

        return BigInt(nodes=normalized, node_size=self.node_size)

    def __mul_bigint(self, other):
        nodes1 = self.nodes
        nodes2 = other.nodes

        # We multiply each node with a list of nodes.
        multiplied = [[a * b for b in nodes2] for a in nodes1]
        # We then pad extra 0s based on digit position
        padded = [a + [0] * (len(multiplied) - i)
                  for i, a in enumerate(multiplied, 1)]
        biginted = [BigInt(nodes=nodes, node_size=self.node_size)
                    for nodes in padded]
        summed = sum(biginted)

        return summed

    def __repr__(self):
        if not self.nodes:
            return '0'
        else:
            stringified = [str(node) for node in self.nodes]
            padded = stringified[:1] + \
                [d.zfill(self.node_size) for d in stringified[1:]]
            return ''.join(padded)


def _chunk_digits(string, node_size, acc=[]):
    if not string:
        return acc
    else:
        return _chunk_digits(string[:-node_size], node_size, [string[-node_size:]] + acc)


def _nodes_normalize(nodes, node_size, carry=0, acc=[]):
    if not nodes:
        if carry > 0:
            return _nodes_normalize([carry], node_size, 0, acc)
        else:
            return acc
    else:
        num = nodes[-1] + carry
        new_num = num % (10 ** node_size)
        new_carry = num // (10 ** node_size)
        return _nodes_normalize(nodes[:-1], node_size, new_carry, [new_num] + acc)
