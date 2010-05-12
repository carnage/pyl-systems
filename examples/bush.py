# -*- coding: utf-8 -*-

from lsystems.symbol.patterns import *

class symbol_lb(branchOpenDrawing,Symbol):
    def __str__(self):
        return '['
        
class symbol_m(rightDrawing,Symbol):
    angle = 22.5
    def __str__(self):
        return '-'      
        
class symbol_rb(branchCloseDrawing,Symbol):
    def __str__(self):
        return ']'
        
class symbol_p(leftDrawing,Symbol):
    angle = 22.5
    def __str__(self):
        return '+'       
        
class symbol_F(simpleRewrite,forwardDrawing,Symbol):
    length = 10
    productions = ['F','F','m','lb','m','F','p','F','p','F','rb','p','lb','p','F','m','F','m','F','rb']


axiom = 'F'

symbols = dict()
symbols['F'] = symbol_F
symbols['p'] = symbol_p
symbols['m'] = symbol_m
symbols['lb'] = symbol_lb
symbols['rb'] = symbol_rb