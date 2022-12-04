#!/usr/bin/python3

def multiple_returns(sentence):
    """
    find the length and first character of a str
    Args:
        sentence - a string
    Return:
        (length, first_char)
    """
    if not sentence:
        return 0, None
    return len(sentence), sentence[0]
