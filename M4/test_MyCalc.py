import unittest
from MyCalc import MyCalc
from unittest.mock import patch

class TestMyCalc(unittest.TestCase):

    def setUp(self):
        self.calc = MyCalc()

    # UCID: sk3298
    # Date: 02/24/2023
    # Description: This test case checks whether the add function correctly adds two numbers and returns the expected result.
    #Series of data is listed below for sample data.
    def test_number_add_number(self):
        result = self.calc.add(2, 3)
        self.assertEqual(result, 5)
        result = self.calc.add(7, 3)
        self.assertEqual(result, 10)
        result = self.calc.add(15, 15)
        self.assertEqual(result, 30)
        result = self.calc.add(10, 15)
        self.assertNotEqual(result, 30)
    
    # UCID: sk3298
    # Date: 02/27/2023
    # Description: This test case checks whether the add function correctly adds two numbers even with using add variable, 
    # which has a value assigned and returns the expected result which is asserted using unittest assert function.
    #Series of data is listed below for sample data.
    def test_ans_add_number(self):
        self.calc.ans = 3
        result = self.calc.add("ans", 2)
        self.assertEqual(result, 5)
        result = self.calc.add("ans", 7)
        self.assertEqual(result, 12)
        result = self.calc.add("ans", 3)
        self.assertEqual(result, 15)
        result = self.calc.add("ans", 1)
        self.assertNotEquals(result, 70)

    # UCID: sk3298
    # Date: 02/27/2023
    # Description: This test case checks whether the sub function correctly subtracts two numbers, 
    # which has a value assigned and returns the expected result which is asserted using unittest assert function.
    #Series of data is listed below for sample data.
    def test_number_sub_number(self):
        result = self.calc.sub(5, 2)
        self.assertEqual(result, 3)
        result = self.calc.sub(20, 10)
        self.assertEqual(result, 10)
        result = self.calc.sub(50, 70)
        self.assertEqual(result, -20)
        result = self.calc.sub(2, 1)
        self.assertNotEqual(result, 8)
    
    # UCID: sk3298
    # Date: 02/27/2023
    # Description: This test case checks whether the test_ans_sub_number function correctly subtracts two numbers, 
    # which has a value assigned and returns the expected result which is asserted using unittest assert function.
    #Series of data is listed below for sample data.
    def test_ans_sub_number(self):
        self.calc.ans = 5
        result = self.calc.sub("ans", 2)
        self.assertEqual(result, 3)
        result = self.calc.sub("ans", 2)
        self.assertEqual(result, 1)
        result = self.calc.sub("ans", 2)
        self.assertEqual(result, -1)
        result = self.calc.sub("ans", 2)
        self.assertNotEqual(result, 3)
    
    # UCID: sk3298
    # Date: 02/27/2023
    # Description: This test case checks whether the test_number_mult_number function correctly multiplies two numbers
    # and returns the expected result which is asserted using unittest assert function.
    #Series of data is listed below for sample data.
    def test_number_mult_number(self):
        result = self.calc.mult(2, 3)
        self.assertEqual(result, 6)
        result = self.calc.mult(5, 5)
        self.assertEqual(result, 25)
        result = self.calc.mult(9, 3)
        self.assertEqual(result, 27)
        result = self.calc.mult(2, 3)
        self.assertNotEqual(result, 0)

    # UCID: sk3298
    # Date: 02/27/2023
    # Description: This test case checks whether the test_mult_ans_number function correctly multiplies two numbers, 
    # the ans variable is used to mutiply with another number, it  has a value assigned and returns the expected result 
    # which is asserted using unittest assert function.
    # Series of data is listed below for sample data.
    def test_mult_ans_number(self):
        self.calc.ans = 3
        result = self.calc.mult("ans", 2)
        self.assertEqual(result, 6)
        result = self.calc.mult("ans", 3)
        self.assertEqual(result, 18)
        result = self.calc.mult("ans", 0)
        self.assertEqual(result, 0)
        result = self.calc.mult("ans", 7)
        self.assertEqual(result, 0)
        result = self.calc.mult("ans", 2)
        self.assertNotEqual(result, 6)

    # UCID: sk3298
    # Date: 02/27/2023
    # Description: This test case checks whether the test_number_div_number function correctly divides two numbers, 
    # the ans variable is used to divide with another number, and returns the expected result 
    # which is asserted using unittest assert function.
    # Series of data is listed below for sample data.
    def test_number_div_number(self):
        result = self.calc.div(100, 5)
        self.assertEqual(result, 20)
        result = self.calc.div(50, 5)
        self.assertEqual(result, 10)
        result = self.calc.div(90, 3)
        self.assertEqual(result, 30)
        result = self.calc.div(6, 3)
        self.assertEqual(result, 2)
        result = self.calc.div(6, 3)
        self.assertNotEqual(result, 1)

    # UCID: sk3298
    # Date: 02/27/2023
    # Description: This test case checks whether the test_ans_div_number function correctly divides two numbers, 
    # the ans variable is used to divide with another number, it  has a value assigned and returns the expected result 
    # which is asserted using unittest assert function.
    # Series of data is listed below for sample data.
    def test_ans_div_number(self):
        self.calc.ans = 250
        result = self.calc.div("ans", 2)
        self.assertEqual(result, 125)
        result = self.calc.div("ans", 5)
        self.assertEqual(result, 25)
        result = self.calc.div("ans", 5)
        self.assertEqual(result, 5)
        result = self.calc.div("ans", 1)
        self.assertEqual(result, 5)
        result = self.calc.div("ans", 9)
        self.assertNotEqual(result, 2)


if __name__ == '__main__':
    unittest.main()
