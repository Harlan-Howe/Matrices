import unittest
from Matrices import Matrix

mat_A = Matrix(((3,4),(6,7)))
mat_B = Matrix.ones((2,2))
mat_A_plus_B_expected = Matrix(((4,5),(7,8)))
mat_4B_expected = Matrix(((4,4),(4,4)))
mat_C = Matrix(((3,5,7),(11,13,17)))
mat_A_times_B_expected = Matrix(((7,7),(13,13)))
mat_A_times_C_expected = Matrix(((53,67,89),(95,121,161)))
mat_D = Matrix(((3,4),))
mat_E = Matrix(((5,9),))
mat_F = Matrix(((1,2,6),))
mat_G = Matrix(((5,-2,8),))
mat_H = Matrix(((28,22,-12),))
mat_I = Matrix.identity(4)
mat_J = Matrix(((2,3,4,5),(12,14,16,18),(-4, 8, 0, -2)))
mat_K = Matrix(((3,4),(5,6),(12,0),(-3,8)))
mat_JK_expected = Matrix(((54,66),(244,276),(34,16)))

class MyTestCase(unittest.TestCase):
    def test_4_sum(self):
        self.assertTrue(mat_A_plus_B_expected.equals(mat_A.add(mat_B)),"A + B was incorrect.")
        self.assertTrue(mat_4B_expected.equals(mat_B.add(mat_B).add(mat_B).add(mat_B)),"B + B + B + B incorrect.")
        with self.assertRaises(AssertionError):
            mat_A.add(mat_C)


    def test_5_scalar_multiply(self):
        self.assertTrue(mat_4B_expected.equals(mat_B.times(4)), f"4B is incorrect. You got {mat_B.times(4)}")

    def test_6_times(self):
        self.assertTrue(mat_A_times_B_expected.equals(mat_A.times(mat_B)), f"A•B is incorrect. You got {mat_A.times(mat_B)}")
        self.assertTrue(mat_A_times_C_expected.equals(mat_A.times(mat_C)),
                        f"A•C is incorrect. You got {mat_A.times(mat_C)}")
        with self.assertRaises(AssertionError):
            mat_A.times(mat_C.transpose())

        with self.assertRaises(AssertionError):
            mat_C.times(mat_A)

    def test_7_dot(self):
        self.assertEqual(51,mat_D.dot(mat_E),f"D•E should be 51. You got {mat_D.dot(mat_E)}")
        with self.assertRaises(AssertionError):
            mat_D.dot(mat_E.transpose())
        self.assertEqual(49,mat_F.dot(mat_G),f"F•G should be 49. You got {mat_F.dot(mat_G)}")

    def test_8_cross(self):
        self.assertTrue(mat_H.equals(mat_F.cross_product(mat_G)), f"F x G should be H. You got {mat_F.cross_product(mat_G)}")

    def test_9_more_times_tests(self):
        self.assertTrue (mat_J.times(mat_I).equals(mat_J), "J * I test failed.")
        self.assertTrue (mat_J.times(mat_K).equals(mat_JK_expected), "J * K gave wrong result.")
        with self.assertRaises(AssertionError):
            mat_K.times(mat_J)

if __name__ == '__main__':
    unittest.main()
