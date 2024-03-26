import numpy


def do_gauss_elimination(A_mat: numpy.ndarray,
                         b_mat: numpy.ndarray) -> numpy.ndarray:
    n = len(b_mat)

    for k in range(0, (n - 1)):
        for i in range((k + 1), n):
            if A_mat[i, k] != 0.0:
                _lambda = A_mat[i, k] / A_mat[k, k]

                A_mat[i, (k +
                          1):n] = A_mat[i,
                                        (k + 1):n] - _lambda * A_mat[k,
                                                                     (k + 1):n]

                b_mat[i] = b_mat[i] - _lambda * b_mat[k]

    for k in range((n - 1), -1, -1):
        b_mat[k] = (b_mat[k] - numpy.dot(A_mat[k, (k + 1):n], b_mat[
            (k + 1):n])) / A_mat[k, k]

    return b_mat


def main():
    A_mat = numpy.array([[2.0, -3.0, -1.0], [3.0, 2.0, -5.0], [1.0, 4.0, -1.0]])
    b_mat = numpy.array([1.0, -1.0, 2.0])

    x_mat = do_gauss_elimination(A_mat=A_mat, b_mat=b_mat)
    print(f"x matrix: {x_mat}")


if __name__ == "__main__":
    main()
