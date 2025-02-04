# Why do we need a class?

shapeA = True
shapeB = 'this is a circle'
shapeC = ('square', -4, 'blue')
shapeD = {'name':'square', 'numSides':4, 'colour':True}

# a class lets us not only capture aspects of a thing, but also validate them
class Shape: # in Python everything ultimately iherits from object
    __slots__ = ('__name', '__numSides', '__dimensions') # NB a one-member tuple MUST have a trailing comma
    # every funtion that belongs to this class MUST take self as an argument
    def __init__(self, name='default', numSides=4, dimensions=(3,4)): # the initializer is called every time we make an instance of this class
        self.name = name # this invokes the property setter (with validation)
        self.numSides = numSides
        self.dimensions = dimensions
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
    @property
    def dimensions(self):
        return self.__dimensions
    @dimensions.setter
    def dimensions(self, new_dimensions):
        '''validate the new dimensions are a tuple o at least two values (+ve int or float)'''
        if type(new_dimensions)==tuple and len(new_dimensions)>1:
            self.__dimensions = [] # we may store as any data type we like - list is mutable (tuple is not)
            # iterate over the tuple members, validating each one
            for i in new_dimensions:
                if type(i) in (int, float) and i>0:
                    self.__dimensions.append(i)
                else:
                    self.__dimensions.append(1) # a sensible default
        else:
            raise TypeError('dimensions must be a tuple of 2 or more values')
    def __str__(self):
        '''The __str__ method is always used when we 'print' an instance'''
        return f'This is a {self.name} with {self.numSides} sides, dimensions {self.dimensions}'

if __name__ == '__main__':
    # here we make instances of our class
    s1 = Shape('square', 4, (3,4)) # in this case 'self' will refer to s1
    s2 = Shape(name='triangle',numSides=3, dimensions=(4,3,2,1))
    # we may access class properties using dot-syntax
    print(s1.name, s2.name)
    print(s1.numSides, s2.numSides)
    # try problems
    s3 = Shape('', -99, ('big', 'small')) # remember - the __init__ is only run ONCE (when we make the instance)
    s3.name = False
    # this next line fails because we set __slots__
    # s3.__name = 'wibblywoo' # here we inadvertently add an additional arbitrary property
    print(s3.name, s3.numSides)
    print(s1, s2, s3)



