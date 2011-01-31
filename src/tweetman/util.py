# -*- coding=utf-8 -*-

def remove_list(from_list, to_list):
    return_list = []
    for from_value in from_list:
        if from_value not in to_list:
           return_list.append(from_value)
    return return_list
