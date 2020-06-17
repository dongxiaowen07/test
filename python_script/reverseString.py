#!/usr/bin/env python
# coding=utf-8


class Stack:
    def __init__(self):
        self.values = []

    def push(self, value):
        self.values.append(value)

    def pop(self):
        return self.values.pop()

    def is_empty(self):
        return self.size() == 0

    def size(self):
        return len(self.values)

    def peak(self):
        return self.values[self.size() - 1]


if __name__ == '__main__':
    aStack = Stack()
    reversedString = []
    aString = raw_input('Please input a string: ')
    '''
    for aChar in aString:
        aStack.push(aChar)

    while not aStack.is_empty():
        reversedString.append(aStack.pop())
    '''
    aString = list(aString)
    while len(aString) != 0:
        reversedString.append(aString.pop())

    reversedString = ''.join(reversedString)
    print 'reversed string: ' + reversedString
