from collections import namedtuple

# create namedtuble object, will be used to create another object
ThreeElmTuble = namedtuple('ThreeElm',['a', 'b', 'c'])

# set deafualts values for tuble members
ThreeElmTuble.__new__.__defaults__ = (1, 2, 3)


