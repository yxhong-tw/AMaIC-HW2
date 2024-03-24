import numpy
import scipy


def main():
    A_mat = numpy.array([[2, -3, 1], [3, 2, -5], [1, 4, -1]])
    _, L_mat, U_mat = scipy.linalg.lu(A_mat)

    L_mat_size = L_mat.shape[0]
    for i in range(1, L_mat_size):
        for j in range(0, i):
            print(f"L[{i + 1}][{j + 1}]: {L_mat[i][j]}")

    U_mat_size = U_mat.shape[0]
    for i in range(U_mat_size):
        for j in range(i, U_mat_size):
            print(f"U[{i + 1}][{j + 1}]: {U_mat[i][j]}")


if __name__ == "__main__":
    main()
