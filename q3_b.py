import numpy
import scipy

from q3_a import print_figure


def get_cubic_spline_func(x: numpy.ndarray, y: numpy.ndarray):
    return scipy.interpolate.CubicSpline(x, y)


def main():
    x = numpy.array([0, 1.2, 2.5, 3.2, 4])
    y = numpy.array([5, 4.1, 3.8, 4.2, 6])

    lp_func = get_cubic_spline_func(x=x, y=y)

    x_new = numpy.array([item for item in numpy.arange(0, 4, 0.2)])
    y_new = lp_func(x_new)

    print_figure(x=x, y=y, x_new=x_new, y_new=y_new, figure_name="Cubic Spline")


if __name__ == "__main__":
    main()
