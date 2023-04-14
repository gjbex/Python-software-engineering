#!/usr/bin/env python

import argparse
import matplotlib.pyplot as plt
import numpy as np
import numpy.typing as npt


def generate_input(a: float | np.float32 | np.float64,
                   b: float | np.float32 | np.float64,
                   n: int | np.int32 | np.int64) -> npt.NDArray[np.float64]:
    '''Generate x-values in given range

    Parameters
    ----------
    a: float
        lower bound
    b: float
        upper bound
    n: int
        number of points to generate

    Returns
    -------
    np.NDarray
        generated x-values
    '''
    return np.linspace(a, b, n)


def gaussian(x: npt.NDArray[np.float64], mu: float, sigma: float) -> npt.NDArray[np.float64]:
    y: npt.NDArray[np.float64] = np.exp(-0.5*(x - mu)**2/sigma)/np.sqrt(2.0*np.pi*sigma)
    return y


def plot_function(x: npt.NDArray[np.float64], y: npt.NDArray[np.float64]) -> None:
    plt.plot(x, y)
    plt.show()
    return


if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser(description='numpy type checking')
    arg_parser.add_argument('--mu', type=float, default=0.0,
                            help='mean value')
    arg_parser.add_argument('--sigma', type=float, default=1.0,
                            help='standard deviation')
    arg_parser.add_argument('--n', type=int, default=10,
                            help='number of points')
    arg_parser.add_argument('--plot', action='set_true',
                            help='show plot')
    options = arg_parser.parse_args()
    x = generate_input(-3.0, 3.0, options.n)
    y = gaussian(x, options.mu, options.sigma)
    if options.plot:
        plot_function(x, y)
    else:
        print(y)
