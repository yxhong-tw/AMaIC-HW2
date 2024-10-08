import numpy

from scipy.sparse.linalg import splu
from typing import Tuple


def calculate_LU(mat: numpy.ndarray) -> Tuple[numpy.ndarray, numpy.ndarray]:
    slu = splu(mat,
               permc_spec="NATURAL",
               diag_pivot_thresh=0,
               options={"SymmetricMode": True})
    L_mat = slu.L.toarray()
    U_mat = slu.U.toarray()

    return L_mat, U_mat


def main():
    A_mat = numpy.array([[2, -3, 1], [3, 2, -5], [1, 4, -1]])
    L_mat, U_mat = calculate_LU(mat=A_mat)

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
