#!/usr/bin/python

def countRecursion(arr):
    if arr == []:
        return 0
    else:
        return 1 + countRecursion(arr[1:])

argArr = []

for i in range(10):
    argArr.append(i)


print argArr
print "Length of argArr: " + str(countRecursion(argArr))
