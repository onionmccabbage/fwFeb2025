# Why do we need a class?

shapeA = True
shapeB = 'this is a circle'
shapeC = ('square', -4, 'blue')
shapeD = {'name':'square', 'numSides':4, 'colour':True}

# a class lets us not only capture aspects of a thing, but also validate them
class Shape:
    __slots__ = ('__name', '__numSides') # NB a one-member tuple MUST have a trailing comma
    # every funtion that belongs to this class MUST take self as an argument
    def __init__(self, name='default', numSides=4): # the initializer is called every time we make an instance of this class
        self.name = name
        self.numSides = numSides
    @property # this is known as decorator syntax
    def name(self):
        '''this is the name getter - is merely returns the name of this instance'''
        return self.__name # we use __ to 'mangle' any actual property name to avoid direct access
    @name.setter
    def name(self, new_name):
        '''this is the name setter - it may validate before persisting the name value'''
        if type(new_name) == str and new_name !='':
            self.__name = new_name
        else:
            self.__name = 'square'
    @property
    def numSides(self):
        return self.__numSides
    @numSides.setter
    def numSides(self, new_numSides): # numSides must be a positive integer
        if type(new_numSides) == int and new_numSides >0:
            #all good - set the value
            self.__numSides = new_numSides
        else:
            self.__numSides = 4 # a sensible default (we could raise a TypeError)

if __name__ == '__main__':
    # here we make instances of our class
    s1 = Shape('square', 4) # in this case 'self' will refer to s1
    s2 = Shape(name='triangle',numSides=3)
    # we may access class properties using dot-syntax
    print(s1.name, s2.name)
    print(s1.numSides, s2.numSides)
    # try problems
    s3 = Shape('', -99) # remember - the __init__ is only run ONCE (when we make the instance)
    s3.name = False
    # this next line fails because we set __slots__
    # s3.__name = 'wibblywoo' # here we inadvertently add an additional arbitrary property
    print(s3.name, s3.numSides)


