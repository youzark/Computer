#!/usr/bin/env python

nums = [1,2,3,4,5,6,7,8,9,10]

def gen_func(nums):
    for num in nums:
        yield num*num

my_gen = gen_func(nums)
for i in my_gen:
    print(i)

my_gen = (num*num for num in nums)
for i in my_gen:
    print(i)
