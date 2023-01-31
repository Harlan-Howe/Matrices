import unittest
from Matrices import Matrix

A = Matrix(((1,2,3),(4,5,6),(7,8,9)))

class MyTestCase(unittest.TestCase):
    def test_2_transpose(self):
        A_T = A.transpose()
        self.assertTupleEqual((3, 3),A_T.shape(),f"A transpose is wrong shape. You got {A_T.shape()}")
        self.assertTrue(A_T.equals(Matrix(((1, 4, 7),
                                  (2, 5, 8),
                                  (3, 6, 9)))), f"A transpose is incorrect. You got {A_T}")

        # TODO: Write at least two more tests to check on other matrices, perhaps non-square ones.
        self.assertTrue(False, "You didn't write this part, did you?")



    def test_3_double_transpose(self):
        self.assertTrue(A.transpose().transpose().equals(A), f"A^T^T should be A. You got {A.transpose().transpose()}")

        #TODO: check that your other matrices work for this, as well.
        self.assertTrue(False, "You didn't write this part, either.")


if __name__ == '__main__':
    unittest.main()
