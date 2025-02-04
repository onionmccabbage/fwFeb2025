from my_shape import Shape

class Figure(Shape):
    '''This Figure class inherists everything from the shape class'''
    # within the __init__ we call the super()
    def __init__(self, name, numSides, dimensions, title):
        super().__init__(name, numSides, dimensions)
        # or
        # Shape.__init__(name, num_sides, dimension)
        self.title = title
        # increment the static property
        Figure.count += 1
    # we would write get.set methods for 'title'
    # here is a static property (belongs to the class, rather than any instance of the class)
    count=0
    @staticmethod
    def howManyInstances():
        '''A static method belongs the class itself (not to any particular instance)'''
        return Figure.count
    def __str__(self):
        msg = super().__str__()
        msg += f' title is {self.title}'
        return msg

if __name__ == '__main__':
    f1 = Figure('Drawing', 7, (3,3), 'Drawing of a shape')
    f2 = Figure('Diagram', 5, (3,3), 'Diagram of a shape')
    f3 = Figure('Illustration', 3, (3,3), 'Illustration of a shape')
    f4 = Figure('Drawing', 99, (3,3), 'Drawing of a shape')
    print(f1)
    # we may call the static method of the class
    print( Figure.howManyInstances() )