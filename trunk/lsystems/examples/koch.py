# -*- coding: utf-8 -*-

from lsystems.symbol.patterns import *


class symbol_F(simpleParametricRewrite,forwardDrawing,Symbol):
    length = 400
    productions = [('F',{'length':lambda self: self.length/3.0}),
		   ('p',{}),
		   ('F',{'length':lambda self: self.length/3.0}),
		   ('m',{}),('m',{}),
		   ('F',{'length':lambda self: self.length/3.0}),
		   ('p',{}),
		   ('F',{'length':lambda self: self.length/3.0})
		  ]

class symbol_p(rightDrawing,Symbol):
    angle = 60

    def __str__(self):
        return '+'
        
class symbol_m(leftDrawing,Symbol):
    angle = 60

    def __str__(self):
        return '-'
        
symbols = dict()
symbols['F'] = symbol_F
symbols['p'] = symbol_p
symbols['m'] = symbol_m

axiom = 'F'