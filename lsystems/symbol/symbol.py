# -*- coding: utf-8 -*-

symbols = dict()

class metaSymbol(type):
    def __call__(cls,*args,**kargs):
        args = list(args)
        args.reverse()
        symbol = args.pop()
        args.reverse()

        obj = cls.__new__(cls, symbol) 
        obj.__init__(*args, **kargs) 
        return obj 

class Symbol(object):
    __metaclass__ = metaSymbol
    gen = 0
    isBranch = False
    isBranchEnd = False
    getctx = [0,0]
    context = 1
    def __new__(cls,symbol):
        cls = 'symbol_'+symbol
        try:
            obj = symbols[symbol]
        except KeyError:
            print symbols
            obj = Symbol
            
        item = object.__new__(obj)
        item.symbol = symbol
        return item
        
    def __str__(self):
        return self.symbol
    
    def setctx(self,ctx,side):
        if side == 'right':
            self.ctxr = ctx
        else:
            self.ctxl = ctx
    
    def rewrite(self):
        return [Symbol(self.symbol)]
        
    def draw(self,t):
        return t