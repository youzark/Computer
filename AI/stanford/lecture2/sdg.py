#! /usr/bin/env python
import numpy as np

######################
#  generate artifical dataset  #
######################
true_w = np.array([1,2,3,4,5])
d = len(true_w)
dataSet = []
for i in range(500000):
    x = np.random.rand(d)
    y = true_w.dot(x)
    dataSet.append((x,y))

######################
#  modeling  #
######################

# dataSet = [(np.array([2]),4),(np.array([4]),2)]
# dimensions = 1

def flaw(w):
    return sum((w.dot(x) - y)**2 for x,y in dataSet) / len(dataSet)

def devFlaw(w):
    return sum(2 * x * (w.dot(x) - y) for x,y in dataSet) / len(dataSet)

def sflaw(w,i):
    x, y = dataSet[i]
    return (w.dot(x) - y)**2

def sdevFlaw(w,i):
    x, y = dataSet[i]
    return 2 * x * (w.dot(x) - y)

#Gradient descent
######################
#  algorithm  #
######################

def gradientDescent(flaw,dev,dimensions):
    w = np.zeros(dimensions)
    eta = 0.05
    for t in range(1000):
        value = flaw(w)
        grad = dev(w)
        w = w - eta * grad
        print(f"iteration{t}: w = {w}, flaw = {value}",flush=True)

def stochasticDescent(sflaw,sdev,dimensions,number):
    w = np.zeros(dimensions)
    eta = 0.01 
    for t in range(1000):
        for i in range(number):
            value = sflaw(w,i)
            grad = sdev(w,i)
            w = w - eta * grad
        print(f"iteration{t}: w = {w}, flaw = {value}",flush=True)

# gradientDescent(flaw,devFlaw,d)
stochasticDescent(sflaw,sdevFlaw,d,len(dataSet))
