import numpy
import scipy

import matplotlib.pyplot as plt


def get_lagrange_polynomial_func(x: numpy.ndarray, y: numpy.ndarray):
    return scipy.interpolate.lagrange(x, y)


def print_figure(x: numpy.ndarray, y: numpy.ndarray, x_new: numpy.ndarray,
                 y_new: numpy.ndarray, figure_name: str):
    figure = plt.figure(figsize=(10, 8))

    plt.plot(x, y, label="Original")
    plt.plot(x_new, y_new, label="New")

    plt.title(figure_name)
    plt.grid()
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend(loc="best")
    plt.show()


def main():
    x = numpy.array([0, 1.2, 2.5, 3.2, 4])
    y = numpy.array([5, 4.1, 3.8, 4.2, 6])

    lp_func = get_lagrange_polynomial_func(x=x, y=y)

    x_new = numpy.array([item for item in numpy.arange(0, 4, 0.2)])
    y_new = lp_func(x_new)

    print_figure(x=x,
                 y=y,
                 x_new=x_new,
                 y_new=y_new,
                 figure_name="Lagrange Polynomial")


if __name__ == "__main__":
    main()
