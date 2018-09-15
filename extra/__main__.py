import sys
from typing import Dict

import kernel


def main():
    args_str = sys.argv[1]
    args = __parse_args(args_str)
    input_path = args.get('input', None)
    digits = args.get('digitsPerNode', None)

    if input_path == None:
        sys.stderr.write('Mixing arg \'input\' from argv')
        sys.stderr.write('Exiting with code (1)')
        sys.exit(1)

    if digits == None:
        sys.stderr.write('Mixing arg \'digitsPerNode\' from argv')
        sys.stderr.write('Exiting with code (2)')
        sys.exit(2)

    inputfile = open(input_path)
    for line in inputfile:
        line = line.strip()
        ast = kernel.string_to_ast(line)
        result = kernel.eval_ast(ast)
        print('%s=%s' % (line, result))

    sys.exit(None)


def __parse_args(string: str) -> Dict[str, str]:
    args = [s.strip() for s in string.split(';')]
    kv_pairs = [a.split('=') for a in args]
    return dict(kv_pairs)


if __name__ == '__main__':
    main()
