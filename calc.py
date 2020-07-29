# -*- coding: utf-8 -*-

def add(*args) :
    return sum(args)

def multiply(*args) :
    result = 1
    for i in args :
        result = result * i
    return result