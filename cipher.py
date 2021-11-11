import sys
import stdio
import stdarray
from instream import InStream
from outstream import OutStream

"""
For example, if input is all capitals
and the keys are THEQUICKBROWN and FXJMPSVRLZYDG,
 then we make this table:
THEQUICKBROWN
FXJMPSVLAZYDG
That is, we should substitute F for T, T for F, H for X, X for H,
and so forth when copying the input to the output. The message is 
encoded by replacing each letter withits pair. For example, the 
message MEET AT ELEVEN is encoded as QJJF BF JKJCJG. Someone receiving 
the message can use the same keys to get the message back.
"""

def map(symbol, arr1, arr2):
    for i in range(len(arr1)):
        if symbol == arr1[i]:
            return str(arr2[i])
        if symbol == arr2[i]:
            return str(arr1[i])
        if symbol == " ":
            return str(" ")

def encode_words(code1, code2):
    instream = InStream('in12.txt')
    text = instream.readAll()
    outstream = OutStream('out12.txt')

    arr1 = stdarray.create1D(len(code1), "")
    arr2 = stdarray.create1D(len(code2), "")

    result = ""
    for i in range(len(code1)):
        arr1[i] = code1[i]
    for i in range(len(code1)):
        arr2[i] = code2[i]
    for i in range(len(text)):
        result += map(text[i], arr1, arr2)

    outstream.write(result)
    return result


def main():
    code1 = sys.argv[1]
    code2 = sys.argv[2]
    "THEQUICKBROWN"
    "FXJMPSVLAZYDG"

    print(encode_words(code1, code2))

if __name__ == '__main__': main()
