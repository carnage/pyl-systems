# -*- coding: utf-8 -*-
from lsystems.symbol.patterns import *

class symbol_x(simpleRewrite,Symbol):
    productions = ['F','m','lb','lb','x','rb','p','x','rb','p','F','lb','p','F','x','rb','m','x']
     
class symbol_F(simpleParametricRewrite,forwardDrawing,Symbol):
    productions = [('F',{'length':lambda self: self.length*2})]        
    length = 3

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
        
axiom = 'x'

symbols = dict()
symbols['x'] = symbol_x
symbols['F'] = symbol_F
symbols['p'] = symbol_p
symbols['m'] = symbol_m
symbols['lb'] = symbol_lb
symbols['rb'] = symbol_rb