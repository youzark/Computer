#!/usr/bin/env python

names = ['Bruce','Clark','Peter','Logan','Wade']
heros = ['Batman','Superman','Spiderman','Wolverine','Deadpool']

my_dict = dict(zip(names,heros))
print(my_dict)

my_dict = {name:hero for name in names for hero in heros}
print(my_dict)
