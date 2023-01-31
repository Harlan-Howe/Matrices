import unittest
from Matrices import Matrix

A = Matrix(((2, 5, 8), (3, 5, 6), (9, 12, 15)))
B = Matrix.identity(3)
C = Matrix(((1,2,3),(4,5,6),(7,8,9)))
D = Matrix.ones((3,5))
class MyTestCase(unittest.TestCase):
    def test_10_determinant(self):
        self.assertEqual(-21, A.determinant(), f"|A| should be -21. You got {A.determinant()}.")
        self.assertEqual(1, B.determinant(), f"|B| should be 1. You got {B.determinant()}.")
        self.assertEqual(0, C.determinant(), f"|C| should be 0. You got {C.determinant()}.")
        with self.assertRaises(AssertionError):
            d = D.determinant()

if __name__ == '__main__':
    unittest.main()
