#!/usr/bin/python3
""" replace a charecter with two new lines.  """


def text_indentation(text):
    """ add two lines after sertain characters.
    checks if input is of string type """
    if type(text) is not str:
        raise TypeError("text must be a string")
    searchList = ['.', '?', ':']
    index = 0
    for place in text:
        if place in searchList:
            if text[index + 1] == " ":
                text = text[:index + 1] + text[index + 2:]
        else:
            index += 1
    index = 0
    for place in text:
        if place in searchList:
            text = text[:index + 1] + '\n\n' + text[index + 1:]
            index += 3
        else:
            index += 1
    print(text, end='')
