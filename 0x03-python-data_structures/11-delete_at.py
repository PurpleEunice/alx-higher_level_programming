#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    """
    deletes an elment from a list at index idx
    Args:
        my_list - list to search
        idx - the position to access
    Return:
        my_list - if idx is out of range
    """

    if idx > -1 and idx < len(my_list):
        del my_list[idx]
    return my_list
