import numpy


def calculate_inverse_matrix(mat: numpy.ndarray) -> numpy.ndarray:
    return numpy.linalg.inv(a=mat)


def calculate_x_matrix(A_mat: numpy.ndarray,
                       b_mat: numpy.ndarray) -> numpy.ndarray:
    A_inv_mat = calculate_inverse_matrix(mat=A_mat)
    return numpy.dot(a=A_inv_mat, b=b_mat)


def main():
    A_mat = numpy.array([[2, -3, 1], [3, 2, -5], [1, 4, -1]])
    b_mat = numpy.array([[1], [-1], [2]])

    x_mat = calculate_x_matrix(A_mat=A_mat, b_mat=b_mat)
    print(f"x matrix: {x_mat}")


if __name__ == "__main__":
    main()
