# import unittest

# def factorize(x):
#     pass

class TestFactorize(unittest.TestCase):
    def test_wrong_types_raise_exception(self):
        inputs = ['string', 1.5]
        for i in inputs:
             with self.subTest(x=i):
                 self.assertRaises(TypeError, factorize, i)
    
    def test_negative(self):
        inputs = [-1, -10, -100]
        for i in inputs:
             with self.subTest(x=i):
                 self.assertRaises(ValueError, factorize, i)
    
    def test_zero_and_one_cases(self):
        inputs = [(0, (0,)), (1, (1,))]
        for i, r in inputs:
            with self.subTest(x=i):
                self.assertEqual(r, factorize(i))
    
    def test_simple_numbers(self):
        inputs = [(3, (3,)), (13, (13,)), (29, (29,))]
        for i, r in inputs:
            with self.subTest(x=i):
                self.assertEqual(r, factorize(i))
    
    def test_two_simple_multipliers(self):
        inputs = [(6, (2,3)), (26, (2,13)), (121, (11,11))]
        for i, r in inputs:
            with self.subTest(x=i):
                 self.assertEqual(r, factorize(i))           

    def test_many_multipliers(self):
        inputs = [(1001, (7, 11, 13)), (9699690, (2,3, 5, 7, 11, 13, 17, 19))]
        for i, r in inputs:
            with self.subTest(x=i):
                 self.assertEqual(r, factorize(i)) 

# if __name__ == '__main__':
#     unittest.main() 