"""A set of functions for working with bigints.
"""


def isbigint(value):
    return isinstance(value, tuple) and len(value) == 3 and value[0] == 'bigint'


def new(nodesize, nodes):
    return ('bigint', nodesize, nodes)
