#! /usr/bin/env python
points = [(2,4),(4,2)]

def flaw(w):
    return sum((w * x - y)**2 for x,y in points)

def devFlaw(w):
    return sum(2 * x * (w * x - y) for x,y in points)

#Gradient descent
w = 0
eta = 0.01

for t in range(100):
    value = flaw(w)
    grad = devFlaw(w)
    w = w - eta * grad
    print(f"iteration{t}: w = {w}, flaw = {value}, grad = {grad}")
