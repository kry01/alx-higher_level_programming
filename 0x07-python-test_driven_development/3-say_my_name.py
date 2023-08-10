#!/usr/bin/python3
"""
say my name scarlet
"""


def say_my_name(first_name, last_name=""):
    """i am not in danger scarlet, i am the danger

    Args:
        first_name (_type_): first name to print
        last_name (str, optional): last name to be printed "".

    Raises:
        TypeError: _description_
        TypeError: _description_
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    elif type(last_name) is not str:
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))
