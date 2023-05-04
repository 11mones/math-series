import pytest
from series.series import Fibonacci
from series.series import lucas
from series.series import sum_series



def test_zero():
    actual= Fibonacci(0)
    expected = 0
    assert actual == expected   



def test_one():
    actual= Fibonacci(1)
    expected = 1
    assert actual == expected

 

def test_two():
    actual= Fibonacci(2)
    expected = 1
    assert actual == expected     

def test_three():
    actual= Fibonacci(3)
    expected = 2
    assert actual == expected      

def test_seven():
    actual= Fibonacci(7)
    expected = 13
    assert actual == expected 


#luacs tests : 


def test_zero():
    actual= lucas(0)
    expected = 2
    assert actual == expected   



def test_one():
    actual= lucas(1)
    expected = 1
    assert actual == expected

 

def test_two():
    actual= lucas(2)
    expected = 3
    assert actual == expected     

def test_three():
    actual= lucas(3)
    expected = 4
    assert actual == expected      

def test_seven():
    actual= lucas(7)
    expected = 29
    assert actual == expected 



#sum_series tests 



def test_zero():
    actual= sum_series(0)
    #this is Fibonacci series
    expected = 0
    assert actual == expected   



def test_five():
    actual= sum_series(6)
    #this is Fibonacci
    expected = 8
    assert actual == expected

 

def test_three_two_one():
    actual= sum_series(3 , 2 , 1)
    #this is lucas
    expected = 4
    assert actual == expected     

def test_four_three_four():
    #this is test of four with 3 and 4 in the base
    actual= sum_series(4 , 3 , 4)
    expected = 18
    assert actual == expected      

def test_five_two_three():
    #this is test of 5 with 2 and 3 in the base
    actual= sum_series(5 , 2 , 3)
    expected = 21
    assert actual == expected 






