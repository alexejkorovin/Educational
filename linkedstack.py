#-----------------------------------------------------------------------
# linkedstack.py
#-----------------------------------------------------------------------

import stdio

# A Stack object is a last-in-first-out collection.

class Stack:

    #-------------------------------------------------------------------

    # Construct an empty Stack object.

    def __init__(self):
        self._first = None  # Reference to first _Node

    #-------------------------------------------------------------------

    # Return True if Stack object self is empty, and False otherwise.

    def isEmpty(self):
        return self._first is None

    #-------------------------------------------------------------------
    def delete(self,k):  #delete item number k
        if self._first == None:
            stdio.writeln("reached the end of stack")
            return

        length = 1
        item = self._first.next
        while item is not None:
            length += 1
            item = item.next
        t=0
        item = self._first
        while t != length - k-1:
            t += 1
            item = item.next
        item.next = item.next.next
        print(item)

    def copy(self):  #copy of the stack without destroying the original
        b = Stack()
        c = Stack()
        item = self._first.next
        while item is not None:
            item = item.next
            b.push(item)
        item = b._first.next
        while item is not None:
            item = item.next
            c.push(item)
        return c

    # delete node at a position

    def deleteNode(self, position):

        # If linked list is empty
        if self._first == None:
            return

            # Store head node
        item = self._first

        # If head needs to be removed
        if position == 0:
            self._first = item.next
            item = None
            return

            # Find previous node of the node to be deleted
        for i in range(position - 1):
            item = item.next
            if item is None:
                break

        # If position is more than number of nodes
        if item is None:
            return
        if item.next is None:
            return

            # Node temp.next is the node to be deleted
        # store pointer to the next of node to be deleted
        next = item.next.next

        # Unlink the node from linked list
        item.next = None

        item.next = next

    # takes a linked-list node and an object
    # item as arguments and removes every node in the list whose item is item.
    def remove(self, s):
        item = self._first
        if self._first == None:
            stdio.writeln("reached the end of stack")
            return
        keys = []
        k = 0
        while item is not None:
            # search for items first
            # if item.next == None:
            #     break
            if item.item == s:
                keys.append(k)
                # item.next = item.next.next
                stdio.writeln(str(item))
            item = item.next
            k +=1
        print(keys)
            #delete items which been found
        # item = self._first

        shift = -1
        for i in range(len(keys)):  # doesnot work correc order of items to delete incorrect
            shift += 1
            self.deleteNode(keys[i]-shift)
        return

        # listmax() that takes the first node in a linked list as
        # an argument and returns the value of the maximum item in the list. Assume that
        # the items are comparable, and return None if the list is empty.

    def listmax(self):
        if self._first == None:
            stdio.writeln("stack is empty")
            return 0
        item = self._first
        max = -32767
        while item is not None:
            if (max < int(item.item)):
                max = int(item.item)
            item = item.next
        return max



    #returns the
    #most recently inserted item on the stack (without popping it)



    def peek(self):
        item = self._first.item
        return item

    # Push item onto the top of 'self'.
    def length(self):
        if self._first == None:
            stdio.writeln("reached the end of stack")
            return 0
        t=1
        item = self._first.next
        while item is not None:
            t += 1
            item = item.next
        return t



    def push(self, item):
        self._first = _Node(item, self._first)

    #-------------------------------------------------------------------zz

    # Pop the top item from 'self' and return it.

    def pop(self):
        if self._first == None:
            stdio.writeln("reached the end of stack")
            return 0
        item = self._first.item
        self._first = self._first.next

        return item



    #-------------------------------------------------------------------

    # Return a string representation of 'self'.

    def __str__(self):
        s = ''
        cur = self._first
        while cur is not None:
            s += str(cur.item) + ' '
            cur = cur.next
        return s

#-----------------------------------------------------------------------

# A _Node object references an item and a next _Node object.
# A Stack object is composed of _Node objects.

class _Node:
    def __init__(self, item, next):
        self.item = item  # Reference to an item.
        self.next = next  # Reference to the next _Node object


#-----------------------------------------------------------------------

# For testing:

def main():
    stack = Stack()
    while not stdio.isEmpty():
        item = stdio.readString()
        # item = "hello 1 2 3"
        if (item == "-" and stack.isEmpty()) or (item == "$" and stack.isEmpty()) or (item == "d" and stack.isEmpty()):
            stdio.writeln("reached the end of stack")
            return
        elif item == "max":
            stdio.writeln("max item in stack is: " + str(stack.listmax()) + ' ')
        elif item == "r":
            stdio.writeln('enter the item to delete')
            k = stdio.readString()
            stdio.writeln(str(stack.remove(k)))
        elif item == "c":
            b = stack.copy()
            stdio.writeln("copy of the stack: ")
            for i in range(b.length()+2):
                stdio.writeln(" " + stack.pop() + ' ')
        elif item == "$":
            stdio.writeln("most recent pushed item is: "+str(stack.peek()) + ' ')
            stdio.writeln("stack length is: "+str(stack.length()))
        elif item == 'd':
            stdio.writeln('enter the number of item to delete')
            k = stdio.readString()
            stack.delete(int(k))
            stdio.writeln("item number "+str(k)+" deleted")
            stdio.writeln("stack length is: " + str(stack.length()))
        elif item == '-':
            stdio.writeln("item popped " + stack.pop() + ' ')
            stdio.writeln("stack length is: "+str(stack.length()))
        else:
            stack.push(item)
            stdio.writeln("item pushed stack length is: " + str(stack.length()))
    stdio.writeln()

if __name__ == '__main__':
    main()
    
#-----------------------------------------------------------------------

# more tobe.txt 
# to be or not to - be - - that - - - is

# python linkedstack.py < tobe.txt 
# to be not that or be 

