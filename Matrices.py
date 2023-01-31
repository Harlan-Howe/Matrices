
# ********************************************************************
#        PART 1
# ********************************************************************

class Matrix:
    def __init__(self,A_in):
        self.mat = A_in

    def shape(self) -> (int,int):
        """
        returns a two-element tuple indicating the number of rows and the number of cols of Matrix A
        :param A_in: an (N x M) matrix
        :return: a tuple consisting of two numbers: (N,M)
        """
        return (len(self.mat), len(self.mat[0]))

    def display(self, message=""):
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

    def __repr__(self)->str:
        return self.__str__()

    def __str__(self) -> str:
        result = ""
        try:
            for line in self.mat:
                result+=(f"{line}\n")
        except TypeError:  # in case this isn't a matrix....
            result = f"Scalar value: {self.mat}"
        return result

    @classmethod  # this means that this is a static "factory" constructor. You say z = Matrix.zeros((5,5)), rather than z.zeros((5,5))
    def zeros(cls, size: (int,
                          int)) -> 'Matrix':  # note single quotes because this is the class, itself and has not been completely defined yet.
        """
        makes an N x M matrix consisting only of zeros
        :param cls: the Matrix class, itself, automatically added, like self normally is, when Matrix.zeros is called.
        :param size: a two-element list or tuple (N x M)
        :return: a N x M matrix
        """
        N = size[0]
        M = size[1]

        assert N > 0 and M > 0, "N and M must be positive."
        return cls([[0 for col in range(M)] for row in range(N)])

    @classmethod  # this means that this is a static "factory" constructor. You say z = Matrix.ones((5,5)), rather than z.ones((5,5))
    def ones(cls, size: (int,
                         int)) -> 'Matrix':  # note single quotes because this is the class, itself and has not been completely defined yet.
        """
        makes an N x M matrix consisting only of ones
        :param cls: the Matrix class, itself, automatically added, like self normally is, when Matrix.zeros is called.
        :param size: a two-element list or tuple (N x M)
        :return: a N x M matrix
        """
        N = size[0]
        M = size[1]
        assert N > 0 and M > 0, "N and M must be positive."
        return cls([[1 for col in range(M)] for row in range(N)])

    @classmethod #this means that this is a static "factory" constructor. You say z = Matrix.identity((5,5)), rather than z.identity((5,5))
    def identity(cls,N:int)-> 'Matrix': #note single quotes because this is the class, itself and has not been completely defined yet.
        """
        creates a diagonal array of ones, (N x N).
        :param cls: the Matrix class, itself, automatically added, like self normally is, when Matrix.zeros is called.
        :param N:
        :return: an (N x N) matrix
        """

        # -------------------------------------------------------
        # TODO: You write this one.
        # I'd suggest that you start by using another method to get a matrix of the right size, and then modify it.



        return Matrix([["Not yet written"]])  # remove this when you add your code.
        # -------------------------------------------------------

    # ********************************************************************
    #        PART 2 (Still in the Matrix class)
    # ********************************************************************

    def transpose(self) -> 'Matrix' :
        """
        creates a new matrix that is A "flipped" on the diagonal axis.
        :return: a (M x N) matrix, that has A's rows and columns swapped.
        """
        # -------------------------------------------------------
        # TODO: You write this one.
        #  Hint: create a matrix of a given size, using one of the methods above, and then update it.


        return Matrix([["Not yet written"]])  # remove this when you add your code.
        # -------------------------------------------------------

    # ********************************************************************
    #        PART 3 (Still in the Matrix class)
    # ********************************************************************

    def add(self, B: 'Matrix') -> 'Matrix':
        """
        creates a new matrix that is the sum of matrices self and B. self and B must have the same shape.
        :param B: a (N x M) matrix
        :return: a new (N x M) Matrix, where (N x M) is the shape of this matrix.
        """
        assert self.shape() == B.shape(), f"For addition, matrices must have same shape. These are {self.shape()} and {B.shape()}."
        # -------------------------------------------------------
        # TODO: You write this one.
        # Remember, you need to create a new matrix to put the results

        return Matrix([["Not yet written"]])  # remove this when you add your code.
        # -------------------------------------------------------

    def times(self, n) -> 'Matrix':
        """
        If n is a scalar, creates a new matrix that is the scalar multiple n·self
        otherwise, if n is a Matrix, performs the dot product of self.dot(n).
        :param n: a scalar number or a matrix.
        :return: a new (N x M) matrix, where (N x M) is the shape of this matrix.
        """
        if type(n) is int or type(n) is float:
            return self.scalar_times(n)
        if type(n) is Matrix:
            return self.matrix_multiply(n)
        else:
            return None

    def scalar_times(self,n:float) -> 'Matrix':
        # -------------------------------------------------------
        # TODO: You write this one.

        return Matrix([["Not yet written"]])  # remove this when you add your code.
        # -------------------------------------------------------

    def matrix_multiply(self, B:'Matrix')->'Matrix':
        """
        performs the matrix multiplication of two matrices
        precondition: self is a (N x M) matrix
        :param B: a (M x P) matrix
        :return: a new (N x P) matrix representing the dot product self·B
        """
        # -------------------------------------------------------
        # TODO: You write this one.

        # write an assertion like the one in add() to make sure this is a viable multiplication.


        # now do the multiplication.




        return Matrix([["Not yet written"]])  # remove this when you add your code.
        # -------------------------------------------------------

    #already finished....
    def equals(self, B:'Matrix', threshold=0) -> bool:
        """
        indicates whether two matrices consist of the same size and contents. If a threshold is provided, then the values in
        the cells can differ by as much as the threshold and still be considered equal.
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
    def dot(self, B:'Matrix') -> 'Matrix':
        """
        performs the dot product of two matrices that are (N x 1) or (1 x N)
        :param B: A matrix of the same shape as A or A^T
        :return:  a scalar number
        """

        A_rows, A_cols = self.shape()
        B_rows, B_cols = B.shape()

        assert A_rows == 1 or A_cols == 1, f"Dot attempted, but self is size {self.shape()}."
        assert B_rows == 1 or B_cols == 1, f"Dot attempted, but B is size {B.shape()}."


        if A_rows > 1:
            return self.transpose().dot(B.transpose())
        assert A_cols == B_cols, f"Dot attempted, but self and B incompatible: self is shape {self.shape()} and B is shape {B.shape()}."
        return self.matrix_multiply(B.transpose()).mat[0][0]

    # already finished....
    def cross_product(self, B:'Matrix') -> 'Matrix':
        """
        finds the cross product of two (1 x 3) matrices (or using the first three values of (1 x N) matrices).
        :param B: a matrix of the same shape as A
        :return: a new (1 x 3) matrix
        """
        assert self.shape() == B.shape(), f"For cross product, shapes should be (1x3) - these are {self.shape()} and {B.shape()}."
        if self.shape()[1] == 1:  # checking for a (3 x 1) matrix, in which case, we'll use the transposes.
            assert self.shape()[0] > 2 , f"self must be at least 3 in one direction. This is {self.shape()}"
            return self.transpose().cross(B.transpose())
        assert self.shape()[1] > 2, f"self must be at least 3 in one direction. This is {self.shape()}"

        return Matrix(((self.mat[0][1] * B.mat[0][2] - self.mat[0][2] * B.mat[0][1],
                self.mat[0][2] * B.mat[0][0] - self.mat[0][0] * B.mat[0][2],
                self.mat[0][0] * B.mat[0][1] - self.mat[0][1] * B.mat[0][0]),))

    # ********************************************************************
    #        PART 4 (Still in the Matrix class)
    # ********************************************************************
    # already written
    def get_minor(self, r:int, c:int) -> 'Matrix':
        """
        returns a smaller array, composed of matrix A, less the given row and column.
        \:param r: number row to remove. r < N
        :param c: number col to remove. c < M
        :return: a array ((N-1) x (M-1)) array
        """
        num_R, num_C = self.shape()
        assert r > -1 and r < num_R and c > -1 and c < num_C, f"Attempting to remove row {r} and col {c} from matrix of shape {self.shape()}."
        rows = []
        for i in range(num_R):
            if i == r:
                continue
            this_row = []
            for j in range(num_C):
                if j == c:
                    continue
                this_row.append(self.mat[i][j])
            rows.append(this_row)
        return Matrix(rows)

    def determinant(self) -> float:
        """
        calculates the determinant of a square matrix
        :param A: a (N x N) matrix
        :return: a scalar
        """
        num_R, num_C = self.shape()
        assert num_R == num_C, f"Determinant must be for a square matrix; this one is {self.shape()}."
        # -------------------------------------------------------
        # TODO: You write this one.
        # Note: this one should be recursive.... make use of the get_minor method immediately above this one!




        pass  # remove this when you add your code.
        # -------------------------------------------------------

    # ********************************************************************
    #        PART 5 (Still in the Matrix class)
    # ********************************************************************
    def inverse(self) -> 'Matrix':
        """
        calculates the inverse of the given square matrix
        :param A: an (N x N) matrix
        :return: a new (N x N) matrix that is the inverse of A, or None, if there is no inverse.
        """
        num_R, num_C = self.shape()
        assert num_R == num_C, f"Must be a square matrix. This one is {self.shape()}."
        # -------------------------------------------------------
        # TODO: You write this one.

        # 1) Construct the minor_matrix. Feel free to make this a separate method.
        

        # 2) Calculate the determinant, either by calling the determinant() method or by using the minor_matrix (faster)



        # 3) The inverse is the transpose of the minor matrix, divided by the determinant. Make sure that the determinant
        #    isn't zero!

        return Matrix([["Not yet written"]])  # remove this when you add your code.
        # -------------------------------------------------------