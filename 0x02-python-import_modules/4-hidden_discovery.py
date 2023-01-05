#!/usr/bin/python3
import hidden_4
import sys
for count in dir(hidden_4):
    if count[:2] != "__":
        print(count)
