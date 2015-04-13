How to use this library

# Symbols file #

To define an L-system, you first need to create a symbols file. There are a few examples in the examples directory; I suggest looking at these to get a feel for how it all works. The symbols file needs to contain three things:

1. A python dictionary named symbols which is a mapping of symbol name to symbol class.
2. A python variable named axiom which is the starting symbol for the system (for axioms longer than one symbol see later)
3. A set of classes defining the symbols in your system.

You should start the file by importing the patterns file.

from lsystems.symbol.patterns import 

# Defining a symbol class #

A symbol class is defined as a standard python class which inherits from the class Symbol.

To be useful it also needs to have some form of production rules; the best way to go about specifying production rules is to use one of the rewrite mix ins, defined in the patterns file. These are described later.

In order to produce an output a symbol also needs a draw method again there are drawing mix ins for the commonly used drawing functions.

# Rewrite mix ins #

For all the mixins, its important that they appear before the Symbol class in the set of classes your class inherits from otherwise the rewrite and draw methods will be overridden.

## No mix in ##
If you inherit from no mix in class and do not define your own rewrite method, the identity production is assumed eg the symbol will rewrite to itself.

## simpleRewrite ##
The simple rewrite is used for Deterministic L-system production rules; this is where a symbol rewrites to one or more symbols in the same way each time. Inherit from the simpleRewrite class to provide a simple rewriting method. To specify the rewrite, you need to define the class variable productions as a list of the names of the symbols you want to rewrite to.

eg:
`productions = ['F','F','m','F','F']`

## randomRewrite ##
The random rewrite is used for Stochastic L-systems. In the same way as above, you need to inherit from the randomRewrite class and define a class variable productions; this time the form is different, it should be a list of tuples each tuple should have the probability of selecting a rule as its first member and a list for the production as its second rule. Probabilities should add up to one.

eg:
`productions = [(.50,['F']),(.50,['F','F'])]`


## simpleParametricRewrite ##
This rewrite is used for simple parametric systems. The structure is again a list of tuples however this time the first member of the tuple should be the symbol to rewrite to, the second member should be a dictionary. This dictionary should contain the name of the property as it key and a lambda function taking the parameter self which returns the value for the property in the next iteration.

eg:
`productions = [('F',{'length':lambda self: self.length +1})]`

# Drawing mix ins #
TODO (for now, look at the examples, its fairly straight forward.)