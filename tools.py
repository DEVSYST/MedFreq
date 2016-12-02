#!/usr/bin/python

def HasStringNumbers(inStr):
    return any(char.isdigit() for char in inStr)