from typing import Any, List, Tuple, Union

Call = Tuple[str, List, List]
AST = Union[Call, Any]

builtins = {
    ('-', 1): lambda args: -args[0],
    ('+', 2): lambda args: args[0] + args[1],
    ('-', 2): lambda args: args[0] - args[1],
    ('*', 2): lambda args: args[0] * args[1],
    ('/', 2): lambda args: args[0] / args[1]
}

operators = set([key[0] for key in builtins.keys()])


def eval_ast(ast: AST) -> Any:
    """Returns the result of evaluating ast.

    If the ast is an invalid expression, an error will occur.

    >>> eval_ast(10)
    10
    >>> eval_ast(('+', [], [4, 5]))
    9
    >>> eval_ast(('+', [], [('+', [], [1, 2]), 3]))
    6
    """
    if isinstance(ast, tuple) and len(ast) == 3:
        return __eval_call(ast)
    else:
        return ast


def __eval_call(call: Call) -> Any:
    name, _, args = call
    arity = len(args)
    key = (name, arity)
    if key in builtins:
        evaled_args = [eval_ast(arg) for arg in args]
        return builtins[key](evaled_args)
    else:
        raise ValueError('No such builtin %s/%d' % (name, arity))


def string_to_ast(string: str) -> AST:
    """Converts a string expression into an ast.

    >>> string_to_ast('200')
    200
    >>> string_to_ast('5 + 4')
    ('+', [], [5, 4])
    >>> string_to_ast('10 * 4 * 3')
    ('*', [], [('*', [], [10, 4]), 3])
    """
    tokens = string_to_tokens(string)
    return tokens_to_ast(tokens)


def string_to_tokens(string: str) -> List[str]:
    """Converts a string expression into its tokens.

    >>> string_to_tokens('1')
    ['1']
    >>> string_to_tokens('2 + 5')
    ['2', '+', '5']
    """
    return __tokenize_str(string, '', [])


def __tokenize_str(string, token, tokens):
    if len(string) == 0:
        tokens.append(token)
        tokens = [t.strip() for t in tokens]
        tokens = [t for t in tokens if t]

        return tokens

    c = string[:1]
    string = string[1:]

    if c.isspace():
        tokens.append(token)
        return __tokenize_str(string, '', tokens)
    elif c in operators:
        tokens.append(token)
        tokens.append(c)
        return __tokenize_str(string, '', tokens)
    else:
        return __tokenize_str(string, token + c, tokens)


def tokens_to_ast(tokens):
    """Converts tokens into an ast.

    >>> tokens_to_ast(['5', '+', '1'])
    ('+', [], [5, 1])
    """
    postfixed = __postfixify_tokens(tokens)

    if len(postfixed) == 0:
        return None

    args = []
    for t in postfixed:
        if t in operators:
            a, b = args.pop(0), args.pop(0)
            ast = (t, [], [a, b])
            args.insert(0, ast)
        else:
            try:
                args.append(int(t))
            except ValueError as e:
                raise e

    return args[0]


def __postfixify_tokens(tokens):
    postfixed = []
    op_stack = []
    for t in tokens:
        if t in operators:
            op_stack.append(t)
        else:
            postfixed.append(t)

    postfixed.extend(op_stack)
    return postfixed
