#!/usr/bin/env python
nums = [1,1,2,3,3,4,5,6,7,6,7,8,9,10]

my_set = set()
for num in nums:
    my_set.add(num)
print(my_set)

my_set = { num for num in nums }
print(my_set)
