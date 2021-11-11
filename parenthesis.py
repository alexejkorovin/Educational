# -----------------------------------------------------------------------
# arraystack.py
# -----------------------------------------------------------------------

import stdio


# A Stack object is a last-in-first-out collection.

class ReverseStack:

    # -------------------------------------------------------------------

    # Construct an empty Stack object.

    def __init__(self):
        self._a = []  # Items

    def size(self):
        return len(self._a)

    # -------------------------------------------------------------------

    # Return True if self is empty, and False otherwise.

    def isEmpty(self):
        return len(self._a) == 0

    # -------------------------------------------------------------------

    # Push object item onto the top of self.

    def push(self, item):
        self._a += [item]

    # -------------------------------------------------------------------

    # Pop the top object from self and return it.

    def pop(self):
        return self._a.pop()

    # -------------------------------------------------------------------

    # Return a string representation self.

    def __str__(self):
        s = ''
        for item in self._a:
            s = str(item) + ' ' + s
        # for item in reversed(self._a):
        #    s += str(item) + ' '
        return s


# Compose a stack client parentheses.py that reads in a text stream from
# standard input and uses a stack to determine whether its parentheses are properly
# balanced. For example, your program should write True for [()]{}{[()()]()}
# and False for [(]).

def main():
    stack1 = ReverseStack()     # for ()
    stack2 = ReverseStack()     # for []
    stack3 = ReverseStack()     # for {}
    # while not stdio.isEmpty():
        # item = stdio.readString()
    item = "(())[]"
    for i in range(len(item)):
        if item[i] == '(':
            stack1.push(item[i])
        if item[i] == '[':
            stack2.push(item[i])
        if item[i] == '{':
            stack3.push(item[i])

        if item[i] == ')':
            stdio.write(stack1.pop() + ' ')
        if item[i] == ']':
            stdio.write(stack2.pop() + ' ')
        if item[i] == '}':
            stdio.write(stack3.pop() + ' ')
        if item[i] == '-':
            break
    print(stack1.isEmpty() and stack2.isEmpty() and stack3.isEmpty())


if __name__ == '__main__':
    main()

# -----------------------------------------------------------------------

# more tobe.txt
# to be or not to - be - - that - - - is

# python3.4 arraystack.py < tobe.txt
# to be not that or be

