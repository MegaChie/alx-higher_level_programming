#!/usr/bin/python3
""" user definned class. """


class Student:
    """ Student to disk and reload """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Student to disk and reload """
        if attrs is None or type(attrs) != list:
            return self.__dict__
        else:
            temp = {}
            for place in attrs:
                if type(place) != str:
                    return self.__dict__
                if place in self.__dict__.keys():
                    temp[place] = self.__dict__[place]
            return temp

    def reload_from_json(self, json):
        """ Student to disk and reload """
        for items in json.keys():
            self.__dict__[items] = json[items]
