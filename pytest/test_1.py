#!/usr/bin/python3
#coding=utf-8

import pytest


# def func(x):
#     return x + 1
    
# def test_answer():
#     assert func(3) == 5

class TestClass:  
    def test_one(self):  
        x = "this"  
        assert 'h' in x  
  
    def test_two(self):  
        x = "hello"  
        assert hasattr(x, 'check')
    
# if __name__ == "__main__":
#     pass