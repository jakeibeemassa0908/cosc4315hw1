"""
Without recursion
"""

import os
import sys
from typing import Dict

import bigint


def main():
    if len(sys.argv) < 2:
        sys.stderr.write('No arguments specified\n')
        sys.stderr.write('Exiting with code (1)\n')
        sys.exit(1)

    args_str = sys.argv[1]
    args = __parse_args(args_str)
    input_path = args.get('input', None)
    digits = args.get('digitsPerNode', None)

    if input_path == None:
        sys.stderr.write('Mixing arg \'input\' from argv\n')
        sys.stderr.write('Exiting with code (2)\n')
        sys.exit(2)

    if digits == None:
        sys.stderr.write('Mixing arg \'digitsPerNode\' from argv\n')
        sys.stderr.write('Exiting with code (3)\n')
        sys.exit(3)

    digits_per_node = int(digits)

    output = run_infinitearithmetic(input_path, digits_per_node)
    print(output)

    sys.exit(None)


def run_infinitearithmetic(input_path, digits_per_node):
    with open(input_path) as inputfile:
        exprs = [line.strip() for line in inputfile]

    result_pairs = [(e, eval_expression(e, digits_per_node)) for e in exprs]
    equations = [(e, result) for e, result in result_pairs if result]
    formatted = ['%s=%s' % (e, bigint.tostring(result))
                 for e, result in equations]
    output = '\n'.join(formatted)

    return output


def eval_expression(expr, digits_per_node):
    expr = expr.strip().replace(" ","")
    if '*' in expr:
        values = expr.split('*')
        x = bigint.parse(values[0], digits_per_node)
        y = bigint.parse(values[1], digits_per_node)
        return bigint.multiply(x, y)

    elif '+' in expr:
        values = expr.split('+')
        x = bigint.parse(values[0], digits_per_node)
        y = bigint.parse(values[1], digits_per_node)
        return bigint.add(x, y)

    else:
        return None


def __parse_args(string: str) -> Dict[str, str]:
    args = [s.strip() for s in string.split(';')]
    kv_pairs = [a.split('=') for a in args]
    return dict(kv_pairs)


if __name__ == '__main__':
    main()
