#!/usr/bin/python3
def element_at(my_list, idx):
    res = my_list[idx:idx + 1]
    if len(res) == 0:
        return None
    else:
        return res[0]
