"""Safe password verification.
Compose a function that takes a string as an
argument and returns True if it meets the
followingconditions, False otherwise:
• At least eight characters long
• Contains at least one digit (0–9)
• Contains at least one uppercase letter
• Contains at least one lowercase letter
• Contains at least one character that is neither a letter nor a number
Such checks are commonly used for passwords on the web

"""

import sys
import stdio
import stdarray
from instream import InStream
from outstream import OutStream


def length(password):
    if len(password) <= 7:
        return False
    else:
        return True


def contain_digit(password):
    for i in range(len(password)):
        if password[i] == "0" or "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9":
            return True
        else:
            return False


def upper_lower_case(password):
    mixed_case = not password.islower() and not password.isupper()
    return mixed_case


def special_char(password):
    if not password.isalnum():
        return True
    else:
        return False


def main():
    password = sys.argv[1]
    print(length(password))
    print(contain_digit(password))
    print(upper_lower_case(password))
    print(special_char(password))


if __name__ == '__main__': main()
