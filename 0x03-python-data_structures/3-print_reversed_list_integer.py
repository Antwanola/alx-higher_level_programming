#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    list_size = len(my_list)
    for i in my_list:
        print("{:d}\n".format(my_list[list_size--))
