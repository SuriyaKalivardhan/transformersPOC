import unittest
from transformersPOC.api import MyMath
from transformersPOC.tt import TT

class TestAdd(unittest.TestCase):
    def test_add(self):
        mm = MyMath()
        res = mm.add(10, 11)
        assert res==21

    def test_concat(self):
        tt = TT()
        res = tt.fn1('Hi', 'Bye')
        assert res == 'Result is HiBye'

if __name__ == '__main__':
    unittest.main()