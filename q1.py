import numpy


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
        condition_number = calculate_condition_number(mat=mat)

        print(f"Condition number of matrix {name}: {condition_number}")

        if condition_number < 10:
            print(f"Matrix {name} is well-conditioned.")
        else:
            print(f"Matrix {name} is ill-conditioned.")

        print()


if __name__ == '__main__':
    main()
