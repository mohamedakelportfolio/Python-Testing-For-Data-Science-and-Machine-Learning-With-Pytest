from collections import namedtuple

import pytest

# create namedtuble object, will be used to create another object
ThreeElmTuble = namedtuple('ThreeElm',['a', 'b', 'c'])

# set deafualts values for tuble members
ThreeElmTuble.__new__.__defaults__ = (1, 2, 3)

@pytest.mark.addition_defaults
def test_defaults():
    """ no parmeters, defaults activation"""
    tet1 = ThreeElmTuble()

    tet2 = ThreeElmTuble(1, 2, 3)

    assert tet1 == tet2

def test_member_acess():
    """check .field functionality of namedtuble"""
    tet = ThreeElmTuble(5, 10)

    assert tet.a == 5
    assert tet.b == 10

    assert (tet.b, tet.c) == (10, 3)

