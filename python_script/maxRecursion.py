#!/usr/bin/python

def maxRecursion(arr):
    if len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]
    sub_max = maxRecursion(arr[1:])
    return arr[0] if arr[0] > sub_max else sub_max

argArr = range(10)

print argArr
print "max of argArr: " + str(maxRecursion(argArr))
