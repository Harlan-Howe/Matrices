import unittest
from Matrices import Matrix

A = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]

class MyTestCase(unittest.TestCase):

    def test_0_Mr_Howes_code(self):
        Mat_A = Matrix(A)
        Mat_Z = Matrix.zeros((2,5))
        self.assertTrue(Mat_Z.equals(Matrix(((0,0,0,0,0),(0,0,0,0,0)))),"Zeros method not working correctly.")

        with self.assertRaises(AssertionError):
            Mat_Z2 = Matrix.zeros((0,2))

        Mat_U = Matrix.ones((4, 4))
        self.assertTrue(Mat_U.equals(Matrix(((1, 1, 1, 1), (1, 1, 1, 1), (1, 1, 1, 1), (1, 1, 1, 1)))),"Ones method not working correctly.")
        with self.assertRaises(AssertionError):
            Mat_U2 = Matrix.ones((-1,0))
        self.assertTupleEqual((4, 3), Mat_A.shape(), f"Shape of A should be (4,3). You got a different shape: {Mat_A.shape()}.")
        self.assertTupleEqual((2, 5), Mat_Z.shape(), f"Shape of Z should be (2,5). You got a different shape: {Mat_Z.shape()}.")
        self.assertTupleEqual((4, 4), Mat_U.shape(), f"Shape of U should be (4,4). You got a different shape: {Mat_U.shape()}.")

    def test_1_Identity(self):
        Mat_I2 = Matrix.identity(2)
        self.assertTrue(Mat_I2.equals(Matrix(((1, 0),
                                     (0, 1)))), f"identity of (2) incorrect. You got {Mat_I2.__repr__()}")

        Mat_I5 = Matrix.identity(5)
        self.assertTrue(Mat_I5.equals(Matrix(((1, 0, 0, 0, 0),
                                     (0, 1, 0, 0, 0),
                                     (0, 0, 1, 0, 0),
                                     (0, 0, 0, 1, 0),
                                     (0, 0, 0, 0, 1)))), f"identity of (5) incorrect. You got {Mat_I5.__repr__()}")

        Mat_I8 = Matrix.identity(8)
        self.assertTrue( Mat_I8.equals(Matrix(((1, 0, 0, 0, 0, 0, 0, 0),
                                     (0, 1, 0, 0, 0, 0, 0, 0),
                                     (0, 0, 1, 0, 0, 0, 0, 0),
                                     (0, 0, 0, 1, 0, 0, 0, 0),
                                     (0, 0, 0, 0, 1, 0, 0, 0),
                                     (0, 0, 0, 0, 0, 1, 0, 0),
                                     (0, 0, 0, 0, 0, 0, 1, 0),
                                     (0, 0, 0, 0, 0, 0, 0,
                                      1)))), f"identity of (8) incorrect. You got {Mat_I8.__repr__()}")





if __name__ == '__main__':
    unittest.main()


"""
Mat_A = Matrix(A)

    Mat_Z = Matrix.zeros((2,5))
    assert Mat_Z.equals(Matrix(((0,0,0,0,0),(0,0,0,0,0)))), f"Z should be ((0,0,0,0,0),(0,0,0,0,0)). You got: {Mat_Z.__repr__()}"

    Mat_U = Matrix.ones((4,4))
    assert Mat_U.equals(Matrix(((1,1,1,1),(1,1,1,1),(1,1,1,1),(1,1,1,1)))), f"U should be ((1,1,1,1),(1,1,1,1),(1,1,1,1),(1,1,1,)). You got {Mat_U.__repr__()}"

    assert Mat_A.shape() == (4,3), f"Shape of A should be (4,3). You got a different shape: {Mat_A.shape()}."
    assert Mat_Z.shape() == (2,5), f"Shape of Z should be (2,5). You got a different shape: {Mat_Z.shape()}."
    assert Mat_U.shape() == (4,4), f"Shape of U should be (4,4). You got a different shape: {Mat_U.shape()}."
    """