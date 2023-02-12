#!/usr/bin/python3
""" 0x0C. Python - Almost a circle """


import json


class Base:
    __nb_objects = 0
    """ Base class """
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Dictionary to JSON string """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ JSON string to file """
        with open(cls.__name__ + ".json", 'w', encoding="utf-8") as fileWrite:
            if list_objs is None:
                fileWrite.write("[]")
            else:
                fileWrite.write(cls.to_json_string([item.to_dictionary()
                                                    for item in list_objs]))
    
    @staticmethod
    def from_json_string(json_string):
        """ JSON string to dictionary """
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Dictionary to Instance """
        if cls.__name__ == "Rectangle":
            temp = cls(1, 1)
        if cls.__name__ == "Square":
            temp = cls(1)
        temp.update(**dictionary)
        return temp

    @classmethod
    def load_from_file(cls):
        """ File to instances """
        result = []
        with open(cls.__name__ + ".json", 'r', encoding="utf-8") as readFile:
            text = readFile.read()
        text = cls.from_json_string(text)
        for item in text:
            if type(item) == dict:
                result.append(cls.create(**item))
            else:
                result.append(item)
        return result
