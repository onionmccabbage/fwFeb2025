# filename.py - this is a Python module (just a text file)
# anything not indented is global
a=2 # this is an int
b=7.3 # this is a float
# + - / *

def someFn():
    '''this is a docstring (documenting the function)'''
    # anything within this code block belongs to this code block
    # stuff here is NOT global
    a=99
    print(f'inside this function the value of a is {a}') # or string.format()

# the very next line that is NOT indented indicattes the end of the that code block
print(f'outside the function the value of a is {a}')

# we may call a function (invoke the function) i.e. make it run
someFn()

# string list tuple dict
# string is an immutable ordinal collection of characters
welcome = """this is
 a string
 with new lines             and tabs
 with a collection of characters"""
print(welcome[0:16:2]) # this is slicing: [n] or [n:m] or [n:m:s] or [:] [n:] [:n]

# list and tuple (all ordinality counts from zero)
t = (3,4,5,6) # this is an imutable ordinal collection of any data values
l = [3,4,5,6] # this is a mutable ordinal collection of any data values

# by the way, everything in Python is an object

l[0] = 'changed' # not allowed for tuples, ok for lists

print(l)

# dictionary or dict is a non-ordinal mutable collection of key:value pairs of any data type
# evertything is in quotes except numbers and boolean
bbc = {'Name':'Floella', 'age':80, 'feature':'Playschool', 'admin':False} # or True
bbc['admin'] = True
print(bbc['Name'], bbc['admin'])

# iteration - or looping
for i in t: # i will be assigned each member of the collection
    print(i)

for i in l:
    print(i)

# for i in welcome:
#     print(i)

# we may iterate over a dict (not ordinal)
for k,v in bbc.items():
    print(k,v)