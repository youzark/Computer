#!/usr/bin/env python3

nums = [1,2,3,4,5,6,7,8,9,10]

my_list = []
for num in nums:
    my_list.append(num)
print(my_list)

my_list = []
my_list = [num for num in nums]
print(my_list)

my_list = []
for num in nums:
    my_list.append(num * num)
print(my_list)

my_list = [num*num for num in nums]
print(my_list)

my_list = list(map(lambda num: num*num , nums))
print(my_list)

my_list = [num for num in nums if num%2 == 0]
print(my_list)

my_list = list(filter(lambda num : num%2 == 0 , nums))
print(my_list)

# all combinations of two elements one from "abcd" and one from "1234"
my_list = []
for letter in "abc":
    for num in range(3):
        my_list.append((letter,num))
print(my_list)

my_list = [(letter,num) for letter in 'abc' for num in range(3)]
print(my_list)


