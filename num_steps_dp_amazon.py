#!/usr/bin/env python3

import time

def helper(n):
    if n == 0 or n == 1:
        return 1
    return helper(n-1) + helper(n-2)

def num_ways(n):
    return helper(n)

def helper_dp(n, memo):
    if n == 0 or n == 1:
        return 1
    if memo[n] != None:
        return memo[n]
    memo[n] = helper_dp(n-1, memo) + helper_dp(n-2, memo)
    return memo[n]

def num_ways_dp(n):
    memo = [None] * (n + 1)
    return helper_dp(n, memo)

# faster but more space
def num_ways_bottom_up(n):
    if n == 0 or n == 1:
        return 1
    nums = [None] * (n + 1)
    nums[0] = 1
    nums[1] = 1
    for i in range(2, n+1):
        nums[i] = nums[i-1] + nums[i-2]
    return nums[n]

# bit slower but less space
def num_ways_bottom_up_3arr(n):
    if n == 0 or n == 1:
        return 1
    nums = [None] * 3
    nums[0] = 1
    nums[1] = 1
    for i in range(2, n+1):
        nums[2] = nums[1] + nums[0]
        nums[0] = nums[1]
        nums[1] = nums[2]
    return nums[2]

#start = time.time()
#for i in range(0,30):
#    print(num_ways(i))
#print('Duration: {} seconds'.format(time.time() - start))

#start = time.time()
#for i in range(0,30):
#    print(num_ways_dp(i))
#print('Duration: {} seconds'.format(time.time() - start))

start = time.time()
for i in range(0,35):
    num_ways_bottom_up(i)
    #print(num_ways_bottom_up(i))
print('Duration: {} seconds'.format(time.time() - start))

start = time.time()
for i in range(0,35):
    num_ways_bottom_up_3arr(i)
    #print(num_ways_bottom_up_3arr(i))
print('Duration: {} seconds'.format(time.time() - start))
