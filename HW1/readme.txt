# cosc4315 homework 1


## How it was solved

We opened the file and read its contents. We then split the input into lines.
These lines get sent into eval_expr for evaluation.
The evaluator looks for multiplication and addition symbols. 
If it finds any of these, it will find the operands and apply the respective operator to them. 
If it finds neither of these, the evaluator raises an error.

Each operand gets converted into a "bigint". A bigint is represented as a 3-tuple. 
The first element is the string 'bigint'. The second element is the nodesize. The third element is the nodes of the bigint.
The bigint addition logic looks to add the nodes together and "split/shift" any nodes greater than the allowed node size.
The multiplication logic takes each node of the second operand and adds the first operand to itself n - 1 number of times.

It then adds 0s to each sum based on its node offset.
It then sums each of these sums to formulate the final multiplied result.
It's done like this to ensure the recursion limit isn't reached. 
Take for example the expression 32183921321 * 489317893479813798341798341798317. 
Surely, the interpreter will hit the recursion limit if it has to recursively repeat 489317893479813798341798341798317 times.

The nodes are stored with the first digits of the number to the very left of the list of nodes.
It's stored this way because lists should be operated left to right style.
When we do need to operate right to left style (eg, printing the number), we reverse the list and do our operations.
The number 159 with a digits per node of 1 would be represented as : ('bigint', 1, [9, 5, 1])

## External packages

No external package was used to solve this problem. 
we use pipenv for project organization

