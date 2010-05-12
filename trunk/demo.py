# -*- coding: utf-8 -*-
from lsystems.generator.basic import basicGenerator
from lsystems.examples import data as example

generator = basicGenerator(example)
generator.run(4)
generator.draw()
