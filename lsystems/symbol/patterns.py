# -*- coding: utf-8 -*-
from lsystems.symbol.symbol import Symbol
import random

class rewriteMixIn:
    pass

class simpleRewrite(rewriteMixIn):
    def rewrite(self):
        return [Symbol(x) for x in self.productions]
        
class randomRewrite(rewriteMixIn):
    def rewrite(self):
        rulenumber = random.random()
        sofar = 0
        for x in self.productions:
            sofar += x[0]
            if rulenumber <= sofar:
                return [Symbol(z) for z in x[1]]

class simpleParametricRewrite(rewriteMixIn):
    def __init__(self,*args,**kwargs):
        for x in kwargs:
	    setattr(self,x,kwargs[x])
	    
    def rewrite(self):
	return [Symbol(x[0],**dict([(y,x[1][y](self)) for y in x[1]])) for x in self.productions]
	
	
    #productions = [('x',{'something':lambda self: self.something/2})

class drawingMixIn:
    pass

class forwardDrawing(drawingMixIn):
    def draw(self,t):
        t[0].forward(self.length)
        return t
        
        
class leftDrawing(drawingMixIn):
    def draw(self,t):
        t[0].left(self.angle)
        return t
        
class rightDrawing(drawingMixIn):
    def draw(self,t):
        t[0].right(self.angle)
        return t
        
        
class branchOpenDrawing(drawingMixIn):        
    def draw(self,t):
        turtle = t[0].clone()
        tmp = [turtle]
        tmp.extend(t)
        return tmp
        
class branchCloseDrawing(drawingMixIn):
    def draw(self,t):
        x=t.pop(0)
        x.ht()
        return t