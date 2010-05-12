# -*- coding: utf-8 -*-
from lsystems.symbol.patterns import *

class symbol_F(randomRewrite,forwardDrawing,Symbol):     
    length = 5
    productions = [(0.33,['F','lb','p','F','rb','F','lb','m','F','rb','F']),
                   (0.33,['F','lb','p','F','rb','F']),
                   (0.34,['F','lb','m','F','rb','F'])
                  ]

class symbol_p(leftDrawing,Symbol):
    angle = 22.5
    def __str__(self):
        return '+'

class symbol_m(rightDrawing,Symbol):
    angle = 22.5      
    def __str__(self):
        return '-' 
        
class symbol_lb(branchOpenDrawing,Symbol):
    def __str__(self):
        return '['
        
class symbol_rb(branchCloseDrawing,Symbol):        
    def __str__(self):
        return ']'

axiom = 'F'

symbols = dict()
symbols['F'] = symbol_F
symbols['p'] = symbol_p
symbols['m'] = symbol_m
symbols['lb'] = symbol_lb
symbols['rb'] = symbol_rb