#!/usr/bin/env python3

def helper(data, k):
    if k == 0:
        return 1

    s = len(data) - k
    if data[s] == "0":
        return 0

    result = helper(data, k - 1)
    if k >= 2 and int(data[s:s+2]) <= 26:
        result += helper(data, k - 2)
    return result

def num_ways(data):
    return helper(data, len(data))

print(num_ways("111111"))
print(num_ways("1111"))
print(num_ways("111"))
print(num_ways("11"))
