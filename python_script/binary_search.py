#!/usr/bin/python
#coding=utf-8

def binarySearch(list, item):
    low = 0
    high = len(list) - 1
    while(low <= high):
        mid = (low + high) / 2 
        guess = list[mid]
        if guess == item:
            return mid
        elif guess < item:
            low = mid + 1
        else:
            high = mid - 1

    return None


def binary_search_recursion(l, aim, start=0, end=None):
    end = len(l)-1 if end is None else end
    if end >= start:
        mid_index = (end -start) // 2 + start
        if aim > l[mid_index]:
            return binary_search_recursion(l,aim,start=mid_index+1,end=end)
        elif aim < l[mid_index]:
            return binary_search_recursion(l,aim,start=start,end=mid_index-1)
        elif aim == l[mid_index]:
            return mid_index            
    else:
        return None

mylist = range(1, 10, 2)
print mylist
print(binarySearch(mylist, 3))
print(binarySearch(mylist, -1))

print "Recursion version of binary_search: "
#print(binarySearchRecursion(mylist, 3))
#print(binarySearchRecursion(mylist, -1))

print "search recursion: "
print(binary_search_recursion(mylist, 3))
print(binary_search_recursion(mylist, -1))
