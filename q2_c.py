import numpy

from q2_a import do_gauss_elimination
from q2_b import calculate_LU


def main():
    A_mat = numpy.array([[2.0, -3.0, -1.0], [3.0, 2.0, -5.0], [1.0, 4.0, -1.0]])
    b_mat = numpy.array([1.0, -1.0, 2.0])

    L_mat, U_mat = calculate_LU(mat=A_mat)

    y = do_gauss_elimination(A_mat=L_mat, b_mat=b_mat)
    x = do_gauss_elimination(A_mat=U_mat, b_mat=y)

    print(f"x matrix: {x}")


if __name__ == "__main__":
    main()
