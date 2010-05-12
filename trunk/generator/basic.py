# -*- coding: utf-8 -*-
import lsystems.symbol.symbol as sym
import turtle

class basicGenerator:
    def __init__(self,system):
        sym.symbols = system.symbols
        self.string = [sym.Symbol(system.axiom)]
        self.config = {'hideturtle':False,'offx':0,'offy':-200}
        
    def run(self,iterations):
        for i in range(iterations):
            newstring = []
            for j in self.string:
                newstring.extend(j.rewrite())

            self.string = newstring
            print str(reduce(lambda x,y:x+y,[str(x) for x in self.string]))


    def turtleConfig(self,config):
        for x in config:
            self.config[x] = config[x]

    def draw(self):
        turtles = [turtle.Turtle()]
        turtle.mode('logo')
        turtles[0].up()
        if self.config['hideturtle']:
            turtles[0].ht()
        turtles[0].speed(0)
        turtles[0].sety(self.config['offy'])
        turtles[0].setx(self.config['offx'])
        turtles[0].down()
        
        for x in self.string:
            turtles = x.draw(turtles)

        raw_input('press return key to exit')