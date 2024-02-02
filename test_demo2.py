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

@pytest.mark.login 
def test_login_fb():
    print("2")
    