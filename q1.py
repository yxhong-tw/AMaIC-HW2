import numpy


def calculate_determinant(mat: numpy.ndarray) -> float:
    return numpy.linalg.det(a=mat)


def calculate_condition_number(mat: numpy.ndarray) -> float:
    return numpy.linalg.cond(x=mat)


def main():
    questions = {
        "(a)":
        numpy.array([[1, 2, 3], [2, 3, 4], [3, 4, 5]]),
        "(b)":
        numpy.array([[2.11, -0.8, 1.72], [-1.84, 3.03, 1.29],
                     [-1.57, 5.25, 4.3]]),
        "(c)":
        numpy.array([[2, -1, 0], [-1, 2, -1], [0, -1, 2]]),
        "(d)":
        numpy.array([[4, 3, -1], [7, -2, 3], [5, -18, 13]])
    }

    for name, mat in questions.items():
        determinant = calculate_determinant(mat=mat)
        if determinant == 0:
            print(f"Matrix {name} is singular.")
        else:
            print(f"Matrix {name} is non-singular (determinant = {determinant}).")

        condition_number = calculate_condition_number(mat=mat)
        if condition_number < 10:
            print(f"Matrix {name} is well-conditioned (condition number = {condition_number}).")
        else:
            print(f"Matrix {name} is ill-conditioned (condition number = {condition_number}).")

        print()


if __name__ == '__main__':
    main()
