"""
根据udacity reviews优化
1. list(zip(*self.g))是一个把二维的数组 的行 和列交换的操作。参考https://blog.csdn.net/u010039733/article/details/48448313
    没有在代码中实现
2. Add(): 一行搞定： Matrix([[self[i][j] + other[i][j] for j in range(self.w)] for i in range(self.h)])
3. Neg: 一行搞定： Matrix([[-self[i][j] for j in range(self.w)] for i in range(self.h)])
"""

import math
from math import sqrt
import numbers

def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)

def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I

class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #############################
 
    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
        
        # TODO - your code here
        rst_determinant = 0
        if self.h == 1:
            rst_determinant = self.g[0][0]
        elif self.h == 2:
            rst_determinant = self.g[0][0]*self.g[1][1] - self.g[0][1]*self.g[1][0]
        return rst_determinant

    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")

        # TODO - your code here
        rst_trace = 0
        for i in range(self.h):
            rst_trace += self.g[i][i]
        return rst_trace

    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")

        # TODO - your code here
        rst_inverse = []
        if self.h == 1:
            rst_inverse = [[1/self.g[0][0]]]
        elif self.h == 2:
            row1 = [self.g[1][1]/self.determinant(), -self.g[0][1]/self.determinant()]
            row2 = [-self.g[1][0]/self.determinant(), self.g[0][0]/self.determinant()]
            rst_inverse.append(row1)
            rst_inverse.append(row2)
        return Matrix(rst_inverse)

    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        # TODO - your code here
        rst_T = []
        for c in range(self.w):
            row = []
            for r in range(self.h):
                row.append(self.g[r][c])
            rst_T.append(row)
        return Matrix(rst_T)

    def is_square(self):
        return self.h == self.w

    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 
        #   
        # TODO - your code here
        #
        # rst_add = []
        # for r in range(self.h):
        #     row = []
        #     for c in range(self.w):
        #         row.append(self.g[r][c] + other.g[r][c])
        #     rst_add.append(row)
        # return Matrix(rst_add)
        return Matrix([[self[i][j] + other[i][j] for j in range(self.w)] for i in range(self.h)])

    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        #   
        # TODO - your code here
        #

        # rst_neg = self.g
        # for r in range(self.h):
        #     for c in range(self.w):
        #         rst_neg[r][c] = -self.g[r][c]
        # return Matrix(rst_neg)
        # 上述会改变原矩阵
        # rst_neg = []
        # for r in range(self.h):
        #     row = []
        #     for c in range(self.w):
        #         row.append(-self.g[r][c])
        #     rst_neg.append(row)
        # return Matrix(rst_neg)
        return Matrix([[-self[i][j] for j in range(self.w)] for i in range(self.h)])

    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        #   
        # TODO - your code here
        #
        rst_sub = []
        for r in range(self.h):
            row = []
            for c in range(self.w):
                row.append(self.g[r][c] - other.g[r][c])
            rst_sub.append(row)
        return Matrix(rst_sub)

    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        #   
        # TODO - your code here
        #

        rst_mul = []
        for r in range(self.h):
            row = []
            for c in range(other.T().h):
                dot = 0
                for i in range(self.w):
                    dot += self[r][i] * other.T()[c][i]
                row.append(dot)
            rst_mul.append(row)
        return Matrix(rst_mul)

    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        if isinstance(other, numbers.Number):
            pass
            #   
            # TODO - your code here
            #
            rst_rmul = []
            for r in range(self.h):
                row = []
                for c in range(self.w):
                    row.append(self.g[r][c] * other)
                rst_rmul.append(row)
            return Matrix(rst_rmul)

if __name__ == '__main__':
    I2 = Matrix([
        [1, 0],
        [0, 1]
    ])
