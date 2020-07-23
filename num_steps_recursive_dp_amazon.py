#!/usr/bin/env python3

import time

def num_ways(n):
    if n == 0 or n == 1:
        return 1
    return num_ways(n-1) + num_ways(n-2)

# does NOT work if n <= 2
def num_ways_x(n):
    if n == 0:
        return 1
    return nums_ways(n-1) + num_ways(n-3) + num_ways(n-5)

def num_ways_x2(n):
    if n == 0:
        return 1
    total = 0
    for i in {1, 3, 5}:
        if n - i >= 0:
            total += num_ways_x2(n - i)
    return total

def num_ways_xbu(n):
    if n == 0:
        return 1
    nums = [None] * (n + 1)
    nums[0] = 1
    for i in range(1, n+1):
        total = 0
        for j in {1, 3, 5}:
            if i - j >= 0:
                total += nums[i - j]
        nums[i] = total
    return nums[n]

start = time.time()
for i in range(0,33):
    #num_ways_x2(i)
    print("{} {}".format(i,num_ways_x2(i)))
print('Duration: {} seconds'.format(time.time() - start))

start = time.time()
for i in range(0,33):
    #num_ways_x2(i)
    print("{} {}".format(i,num_ways_xbu(i)))
print('Duration: {} seconds'.format(time.time() - start))
