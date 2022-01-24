#!/usr/bin/env python
# lambda input: return
lambda x: 3*x + 1

full_name = lambda full_name, last_name: f"{full_name.strip().title()} {last_name.strip().title()}"
print(full_name("  h"," yx"))

scifi_authors = ['Issac Asimov','Ray Bradbury','Robert Heinlein','Arthus C. Clarke']

scifi_authors.sort(key=lambda name: name.split(' ')[-1].lower())
print(scifi_authors)

# write function that buld functions
def build_quadratic_function(a,b,c):
    return lambda x: a*x**2 + b*x + c

f = build_quadratic_function(1,1,1)

print(f(4))
