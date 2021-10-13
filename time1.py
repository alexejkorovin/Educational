"""
Time. Develop a data type for the time of day. Provide client methods that
return the current hour, minute, and second, as well as a __str__() method.
Develop two implementations: one that keeps the time as a single int value (number
of seconds since midnight) and ano
"""
import time


# class Time:



def main():
    named_tuple = time.localtime()  # get struct_time
    time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)
    print(named_tuple)
    print(time_string)

if __name__ == '__main__':
        main()