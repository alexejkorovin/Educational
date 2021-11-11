# -----------------------------------------------------------------------
# lookup.py
# -----------------------------------------------------------------------

import sys
import stdio
from instream import InStream
from hashst import SymbolTable
from bst import OrderedSymbolTable
# -----------------------------------------------------------------------
# 1 Modify lookup.py to make a program lookupandput.py that allows put
# operations to be specified on standard input. Use the convention that a plus sign
# indicates that the next two strings typed are the key–value pair to be inserted.\
# -----------------------------------------------------------------------

# Accept string inStream, integer keyField, and integer valField as
# command-line arguments. inStream is the name of a file. Each line
# of the file contains fields separated by commas. keyField identifies
# which field of each line is a key, and valField identifies which
# field of each line is a value. Use the keys and values to create a
# symbol table. Then read a key from standard input, search
# the symbol table for the key, and write to standard output the
# key's value or 'not found' as appropriate. Repeat until end-of-file
# of standard input.

inStream = InStream(sys.argv[1])
keyField = int(sys.argv[2])
valField = int(sys.argv[3])

# Build a database from inStream.
database = inStream.readAllLines()

# Extract keys and values from the database and add them to st.
st = SymbolTable()
for line in database:
    tokens = line.split(',')
    key = tokens[keyField]
    val = tokens[valField]
    st[key] = val

# Read keys, search st, and write values.
while not stdio.isEmpty():
    query = stdio.readString()

    for key in st:
        if st[key] == query:
            stdio.writeln(key + " : "+st[key])
        else:
            stdio.writeln('value not found')

    # bst = OrderedSymbolTable()
    # for key in st:
    #     index = st[key]
    #     if index == query:
    #         if not index in st:
    #             bst[index] = []
    #         bst[index] += [key]
    #     else:
    #         stdio.writeln('type value: ')
    #         value = stdio.readString()
    #         st[query] = value
    #         stdio.writeln("new key - val: "+ st[query])
    # stdio.writeln(index)
# -----------------------------------------------------------------------

# python lookup.py amino.csv 0 3
# TTA
# Leucine
# ABC
# Not found
# TCT
# Serine

# python lookup.py amino.csv 3 0
# Glycine
# GGG

# python lookup.py ip.csv 0 1
# google.com
# 64.233.167.99

# python lookup.py ip.csv 1 0
# 64.233.167.99
# google.com

# python lookup.py djia.csv 0 1
# 29-Oct-29
# 252.38

