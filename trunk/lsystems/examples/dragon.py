# -*- coding: utf-8 -*-
from lsystems.symbol.patterns import *

class symbol_x(simpleRewrite,Symbol):
    productions = ['F','x','p','F','y']
        
class symbol_y(simpleRewrite,Symbol):
    productions = ['F','x','m','F','y']
        
class symbol_F(simpleRewrite,forwardDrawing,Symbol):
    productions = []
    length = 10

class symbol_p(rightDrawing,Symbol):
    angle = 90

class symbol_m(leftDrawing,Symbol):
    angle = 90
    
axiom = 'x'

symbols = dict()
symbols['x'] = symbol_x
symbols['y'] = symbol_y
symbols['F'] = symbol_F
symbols['p'] = symbol_p
symbols['m'] = symbol_m
