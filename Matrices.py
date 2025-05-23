import logging
from typing import List, Optional

# ********************************************************************
#        PART 1
# ********************************************************************
from KinkaidDecorators import log_start_stop_method

# logging.basicConfig(level=logging.INFO) # simple version to the output console
logging.basicConfig(level=logging.DEBUG, filename="log.txt", format="%(asctime)s %(levelname)s %(message)s",
                    datefmt="%b %e, %Y @ %H:%M:%S %p --- ")  # more robust, sent to a file called log.txt in project


class Matrix:
    def __init__(self, A_in: List[List]):
        self.mat = A_in

    def shape(self) -> (int, int):
        """
        returns a two-element tuple indicating the number of rows and the number of cols of Matrix A.
        :return: a tuple consisting of two numbers: (N,M) for the shape of the self matrix.
        """
        return len(self.mat), len(self.mat[0])

    def display(self, message: str = ""):
        """
        a quick printing routine that puts a dividing line before and after the matrix, along with an optional title.
        :param message:
        :return:
        """
        print("-" * (79 - len(message)), end=" ")
        print(message)
        if self.mat is None:
            print("None")
        else:
            print(self.__repr__())
        print("=" * 80)

    def __repr__(self) -> str:
        return self.__str__()

    def __str__(self) -> str:
        result = ""
        try:
            for line in self.mat:
                result += f"{line}\n"
        except TypeError:  # in case this isn't a matrix....
            result = f"Scalar value: {self.mat}"
        return result

    @classmethod  # this means that this is a static "factory" constructor. You say z = Matrix.zeros((5,5)),
    # rather than z.zeros((5,5))
    def zeros(cls, size: (int,
                          int)) -> 'Matrix':  # note single quotes because this is the class, itself and has not been
        # completely defined yet.
        """
        makes an N x M matrix consisting only of zeros
        :param cls: the Matrix class, itself, automatically added, like self normally is, when Matrix.zeros() is called.
        :param size: a two-element list or tuple (N x M)
        :return: an N x M matrix
        """
        N = size[0]
        M = size[1]

        assert N > 0 and M > 0, "N and M must be positive."
        return cls([[0 for col in range(M)] for row in range(N)])

    @classmethod  # this means that this is a static "factory" constructor. You say z = Matrix.ones((5,5)), rather
    # than z.ones((5,5))
    def ones(cls, size: (int,
                         int)) -> 'Matrix':  # note single quotes because this is the class, itself and has not been
        # completely defined yet.
        """
        makes an N x M matrix consisting only of ones
        :param cls: the Matrix class, itself, automatically added, like self normally is, when Matrix.zeros() is called.
        :param size: a two-element list or tuple (N x M)
        :return: an N x M matrix
        """
        N = size[0]
        M = size[1]
        assert N > 0 and M > 0, "N and M must be positive."
        return cls([[1 for col in range(M)] for row in range(N)])

    @classmethod  # this means that this is a static "factory" constructor. You say z = Matrix.identity((5,5)), rather
    # than z.identity((5,5))
    def identity(cls, N: int) -> 'Matrix':  # note single quotes because this is the class, itself, and has not been
        # completely defined yet.
        """
        creates a diagonal array of ones, (N x N).
        :param cls: the Matrix class, itself, automatically added, like self normally is, when Matrix.zeros() is called.
        :param N:
        :return: an (N x N) matrix
        """

        # -------------------------------------------------------
        # TODO: You write this one.
        # I'd suggest that you start by using another method to get a matrix of the right size, and then modify it.

        return Matrix([["identity not yet written"]])  # remove this when you add your code.
        # -------------------------------------------------------

    # ********************************************************************
    #        PART 2 (Still in the Matrix class)
    # ********************************************************************

    @log_start_stop_method
    def transpose(self) -> 'Matrix':
        """
        creates a new matrix that is A "flipped" on the diagonal axis.
        :return: a (M x N) matrix, that has A's rows and columns swapped.
        """
        # -------------------------------------------------------
        # TODO: You write this one.
        #  Hint: create a matrix of a given size, using one of the methods above, and then update it.
        logging.debug("Doing the transpose.... (an example debug message.")

        return Matrix([["Transpose not yet written"]])  # remove this when you add your code.
        # -------------------------------------------------------

    # ********************************************************************
    #        PART 3 (Still in the Matrix class)
    # ********************************************************************

    @log_start_stop_method
    def add(self, B: 'Matrix') -> 'Matrix':
        """
        creates a new matrix that is the sum of matrices self and B. self and B must have the same shape.
        :param B: a (N x M) matrix
        :return: a new (N x M) Matrix, where (N x M) is the shape of this matrix.
        """
        assert self.shape() == B.shape(), (f"For addition, matrices must have same shape. These are {self.shape()} and "
                                           f"{B.shape()}.")
        # -------------------------------------------------------
        # TODO: You write this one.
        # Remember, you need to create a new matrix to put the results

        return Matrix([["Add not yet written"]])  # remove this when you add your code.
        # -------------------------------------------------------

    @log_start_stop_method
    def times(self, n) -> Optional['Matrix']:
        """
        If n is a scalar, creates a new matrix that is the scalar multiple n·self
        otherwise, if n is a Matrix, performs the dot product of self.dot(n).
        :param n: a scalar number or a matrix.
        :return: either a new (N x M) matrix, where (N x M) is the shape of this matrix (if scalar) OR
        a new (N x P) matrix representing the dot product self·n if self is (N x M) and n is (M x P).
        """
        if type(n) is int or type(n) is float:
            return self.scalar_times(n)
        if type(n) is Matrix:
            return self.matrix_multiply(n)
        else:
            return None

    @log_start_stop_method
    def scalar_times(self, n: float) -> 'Matrix':
        """
        creates a new matrix that is the scalar multiple of n·self.
        :param n: the scalar multiple
        :return: a new (N x M) matrix, where (N x M) is the shape of this matrix.
        """
        # -------------------------------------------------------
        # TODO: You write this one.

        return Matrix([["Times not yet written"]])  # remove this when you add your code.
        # -------------------------------------------------------

    @log_start_stop_method
    def matrix_multiply(self, B: 'Matrix') -> 'Matrix':
        """
        performs the matrix multiplication of two matrices (not to be confused with the cell-wise multiplication)
        precondition: self is a (N x M) matrix
        :param B: a (M x P) matrix
        :return: a new (N x P) matrix representing the matrix product self·B
        """
        # -------------------------------------------------------
        # TODO: You write this one.

        # write an assertion like the one in add() to make sure this is a viable multiplication.

        # now do the multiplication.

        # (Note: don't just call the dot product, because it is calling this method and you'll get runaway mutual
        # recursion.)

        return Matrix([["Matrix Multiply not yet written"]])  # remove this when you add your code.
        # -------------------------------------------------------

    # already finished....
    def equals(self, B: 'Matrix', threshold=0) -> bool:
        """
        indicates whether two matrices consist of the same size and contents. If a threshold is provided, then the
        values in the cells can differ by as much as the threshold and still be considered equal.
        :param B: a (P x Q) matrix
        :param threshold: a scalar, presumably a small one
        :return: whether N == P and M == Q and each item of the two matrices matches to within threshold.
        """
        A_rows, A_cols = self.shape()
        B_rows, B_cols = B.shape()

        if A_rows != B_rows or A_cols != B_cols:
            return False

        for i in range(A_rows):
            for j in range(A_cols):
                if abs(self.mat[i][j] - B.mat[i][j]) > threshold:
                    return False
        return True

    # already finished....
    def dot(self, B: 'Matrix') -> int:
        """
        performs the dot product of two matrices that are (N x 1) or (1 x N)
        :param B: A matrix of the same shape as A or A^T
        :return:  a scalar number
        """

        A_rows, A_cols = self.shape()
        B_rows, B_cols = B.shape()

        assert A_rows == B_rows and A_cols == B_cols, f"Dot attempted, but A is size {self.shape()} and B is size {B.shape()}."
        assert A_rows == 1 or A_cols == 1, f"Dot attempted, but self is size {self.shape()}."

        if A_rows > 1:
            return self.transpose().matrix_multiply(B).mat[0][0]

        return self.matrix_multiply(B.transpose()).mat[0][0]



    # already finished....
    def cross_product(self, B: 'Matrix') -> 'Matrix':
        """
        finds the cross product of two (1 x 3) matrices (or using the first three values of (1 x N) matrices).
        :param B: a matrix of the same shape as A.
        :return: a new (1 x 3) matrix
        """
        assert self.shape() == B.shape(), (f"For cross product, shapes should be (1x3) - these are {self.shape()} "
                                           f"and {B.shape()}.")
        if self.shape()[1] == 1:  # checking for a (3 x 1) matrix, in which case, we'll use the transposes.
            assert self.shape()[0] > 2, f"self must be at least 3 in one direction. This is {self.shape()}"
            return self.transpose().cross(B.transpose())
        assert self.shape()[1] > 2, f"self must be at least 3 in one direction. This is {self.shape()}"

        return Matrix([[self.mat[0][1] * B.mat[0][2] - self.mat[0][2] * B.mat[0][1],
                        self.mat[0][2] * B.mat[0][0] - self.mat[0][0] * B.mat[0][2],
                        self.mat[0][0] * B.mat[0][1] - self.mat[0][1] * B.mat[0][0]],])

    # ********************************************************************
    #        PART 4 (Still in the Matrix class)
    # ********************************************************************
    # already written
    def get_minor(self, r: int, c: int) -> 'Matrix':
        """
        returns a smaller array, composed of matrix A, less the given row and column.
        precondition: self is an N x M matrix.
        :param r: number row to remove. r < N
        :param c: number col to remove. c < M
        :return: an array ((N-1) x (M-1)) array
        """
        num_r, num_c = self.shape()
        assert -1 < r < num_r and -1 < c < num_c, \
            f"Attempting to remove row {r} and col {c} from matrix of shape {self.shape()}."
        rows = []
        for i in range(num_r):
            if i == r:
                continue
            this_row = []
            for j in range(num_c):
                if j == c:
                    continue
                this_row.append(self.mat[i][j])
            rows.append(this_row)
        return Matrix(rows)

    @log_start_stop_method
    def determinant(self) -> float:
        """
        calculates the determinant of a square matrix
        Precondition: self is a square matrix.
        :return: a scalar
        """
        num_r, num_c = self.shape()
        assert num_r == num_c, f"Determinant must be for a square matrix; this one is {self.shape()}."
        # -------------------------------------------------------
        # TODO: You write this one.
        # Note: this one should be recursive.... make use of the get_minor method immediately above this one!

        # -------------------------------------------------------
        return -1  # remove this when you add your code.

    # ********************************************************************
    #        PART 5 (Still in the Matrix class)
    # ********************************************************************
    @log_start_stop_method
    def inverse(self) -> 'Matrix':
        """
        calculates the inverse of the given square matrix
        precondition: self is a square matrix
        :return: a new (N x N) matrix that is the inverse of A, or None, if there is no inverse.
        """
        num_r, num_c = self.shape()
        assert num_r == num_c, f"Must be a square matrix. This one is {self.shape()}."
        # -------------------------------------------------------
        # TODO: You write this one.

        # 1) Construct the minor_matrix. (Remember, this is different from just the minor.)
        # Feel free to make this a separate method and call it from here.

        # 2) Calculate the determinant, either by calling the determinant() method or by using the minor_matrix (faster)

        # 3) The inverse is the transpose of the minor matrix, times the signs matrx, divided by the determinant. Make sure that the
        #    determinant isn't zero!

        return Matrix([["Inverse not yet written"]])  # remove this when you add your code.
        # -------------------------------------------------------

