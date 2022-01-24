#!/usr/bin/env python
import abc

class MyInterFace(abc.ABC):
    @abc.abstractmethod
    def func1(self):
        pass

class MyClass(MyInterFace):
    def func1(self):
        print("hello world")

test = MyClass()
test.func1()
