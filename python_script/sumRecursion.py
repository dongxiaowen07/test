#!/usr/bin/python

def sumRecursion(arr):
    if arr == []:
        return 0
    else:
        return arr[0] + sumRecursion(arr[1:])

argArr = []
for i in range(1, 11):
    argArr.append(i)

print "sum of 1..10: " + str(sumRecursion(argArr))

