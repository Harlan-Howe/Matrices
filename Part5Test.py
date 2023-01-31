import unittest
from Matrices import Matrix

A = Matrix([[4,2,9],[-1,4,7],[8,3,0]])
A_inv_expected = Matrix([[21/287, -27/287, 22/287],
                  [-56/287, 72/287, 37/287],
                  [35/287, -4/287, -18/287]])

B = Matrix([[5],[-2], [9]])

C = Matrix([[2,4,6],
           [8,10,12],
           [14,16,18]])
class MyTestCase(unittest.TestCase):
    def test_11_inverse(self):

        #Note: I'm adding a threshold here in equals, since we are multiplying floats and may encounter small rounding
        # errors The threshold is saying "the numbers are equal, give-or-take this amount."
        self.assertTrue(A_inv_expected.equals(A.inverse(),threshold= 1E-4),f"A_inv is incorrect.")
        self.assertTrue(Matrix.identity(3).equals(A.times(A.inverse()),threshold= 1E-4),f"A•A^-1 should be I.")
        self.assertTrue(Matrix.identity(3).equals(A.inverse().times(A),threshold= 1E-4),f"A•A^-1 should be I.")

        self.assertIsNone(C.inverse())

    def test_12_solve_equation(self):
        # solve         A * x = B
        #        A^-1 * A * x = A^-1 * B      multiply A^-1 by each side
        #               I * x = A^-1 * B      simplify A^-1 * A = I
        #                   x = A^-1 * B      I is multiplicative identity

        x = A.inverse().times(B)

        self.assertTrue(A.times(x).equals(B, threshold=1E-4), "x does not satisfy A*x = B")

if __name__ == '__main__':
    unittest.main()
