from typing import Iterable


def flatten(iterable):
    flat_list = []
    for int_or_list in iterable:
        if isinstance(int_or_list, list):
            flat_list += flatten(int_or_list)
        if isinstance(int_or_list, int):
            flat_list.append(int_or_list)
    return flat_list

iterable = [None, None, 3]
print(flatten(iterable))