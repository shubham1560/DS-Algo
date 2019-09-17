# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 21:29:59 2019

@author: shubhamsinha01
"""

#kickoff with the classic factorial example

def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
    
    
