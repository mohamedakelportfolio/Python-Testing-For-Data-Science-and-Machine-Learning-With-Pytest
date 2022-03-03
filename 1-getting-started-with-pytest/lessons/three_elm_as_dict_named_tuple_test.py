from collections import namedtuple
import pytest

# create namedtuble object, will be used to create another object
ThreeElmTuble = namedtuple('ThreeElm',['a', 'b', 'c'])

# set deafualts values for tuble members
ThreeElmTuble.__new__.__defaults__ = (1, 2, 3)

def test_asdict():
    """asdict() should return a dictionary"""

    tet_tuple = ThreeElmTuble(10, 20, 30)
    tet_dict = tet_tuple._asdict()

    expected = {'a':10, 'b':20, 'c':30}

    assert tet_dict == expected

@pytest.mark.multiplication_replace
def test_replace():
    """replace should change passed in field"""

    tet_before = ThreeElmTuble(100,200,300)
    tet_after = tet_before._replace(a =1000, b=2000)
    tet_expected = ThreeElmTuble(1000, 2000, 300)

    assert tet_after == tet_expected