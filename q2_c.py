import numpy

from q2_a import calculate_x_matrix
from q2_b import calculate_LU


def main():
    A_mat = numpy.array([[2, -3, 1], [3, 2, -5], [1, 4, -1]])
    b_mat = numpy.array([[1], [-1], [2]])

    L_mat, U_mat = calculate_LU(A_mat)

    y = calculate_x_matrix(L_mat, b_mat)
    x = calculate_x_matrix(U_mat, y)

    print(f"x matrix: {x}")


if __name__ == "__main__":
    main()
