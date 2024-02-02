import pytest

def test_m1():
    assert "ganesh" == "GANESH"


def test_m2():
    a = 1
    b = 2
    assert a+1 == 2 ,"It Right" 

def test_m3():
    name = "selenium"
    assert name.upper == "SELENIUM"

@pytest.mark.login                      # mark is use to mark the test case and login is the name assign to the mark
def test_login_insta():
    print("1")

# to run this file just hit the below syntax in your cmd...
# py.test test_login.py -m login