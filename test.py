import pytest
from jumble import power_list, permute

def test_power_list():
    s = power_list(['a'])
    assert s == [[],['a']]
    t = power_list(['a','b'])
    assert ['a'] in t
    assert ['b'] in t
    assert ['b','a'] in t

def test_permute():
    ans = permute('do')
    assert ans == ['do', 'od']
