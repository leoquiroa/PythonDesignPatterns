#!/usr/bin/python
# -*- coding: utf-8 -*-
import json

#Model
class Person(object):

    def __init__(self, first_name=None, last_name=None):
        self.first_name = first_name
        self.last_name = last_name

   # returns Person name, ex: John Doe
    def name(self):
        return '%s %s' % (self.first_name, self.last_name)

   # returns all people inside db.txt as list of Person objects
    @classmethod
    def getAll(self):
        result = []
        json_list = []
        #generate data
        for i in range(0,5):
            json_element = {"first_name": i, "last_name": i}
            json_list.append(json_element)
        #read it
        for item in json_list:
            person = Person(item['first_name'], item['last_name'])
            result.append(person)
        return result

class View():

    def showAllView(self,list):
        print('In our db we have %i users. Here they are:' % len(list))
        for item in list:
            print(item.name())

    def startView(self):
        print('MVC - the simplest example')
        print('Do you want to see everyone in my db?')

    def endView(self):
        print('Goodbye!')

class Control():

    def __init__(self):
        self.view = View()

    def start(self):    
        self.view.startView()
        key_in = input("[y/n] ") 
        if key_in == 'y':
            return self.showAll()
        else:
            return self.view.endView()

    def showAll(self):
        # gets list of all Person objects
        people_in_db = Person.getAll()
        # calls view
        return self.view.showAllView(people_in_db)


if __name__ == '__main__':
    control = Control()
    # running controller function
    control.start()
