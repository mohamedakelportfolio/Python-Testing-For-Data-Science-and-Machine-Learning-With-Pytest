import pandas as pd

# load csv into dataframe
ssn = list(pd.read_csv("1-unit-testing-assert-statement/exercises/data/ssn.csv"))


def test_all_records():
    assert ssn == ['218-68-9955', '165-73-3124', '432-47-4043', '563-93-1393', '153-93-3401',
                   '670-09-7369', '123-05-9652', '812-13-2476', '726-13-1007', '825-05-4836']


def test_first_record():
    assert ssn[0] == "218-68-9955"


def test_first_record_instance():
    assert isinstance(ssn[0], str)


def test_last_record1():
    assert ssn[len(ssn)-1] == "825-05-4836"
    assert isinstance(ssn[len(ssn)-1], str)


def test_last_record2():
    assert ssn[-1] == "825-05-4836"
    assert isinstance(ssn[-1], str)


def test_two_records():
    assert ssn[1:3] == ['165-73-3124', '432-47-4043']


def test_reversed_records1():
    assert ssn[-2:] == ['726-13-1007', '825-05-4836']


def test_all_except_two():
    assert ssn[:-2] == ['218-68-9955', '165-73-3124', '432-47-4043',
                        '563-93-1393', '153-93-3401', '670-09-7369', '123-05-9652', '812-13-2476']
def test_custom_cols_rows():
    assert ssn[-1::-1]