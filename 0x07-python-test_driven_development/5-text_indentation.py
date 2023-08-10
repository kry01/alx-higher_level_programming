#!/usr/bin/python3

"""function
"""


def text_indentation(text):
    """

    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    for sep in ".:?":
        text = (sep + "\n\n").join(
            [line.strip(" ") for line in text.split(sep)])

    print("{}".format(text), end="")
