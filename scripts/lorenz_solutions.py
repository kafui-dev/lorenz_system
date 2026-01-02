import numpy as np
import matplotlib.pyplot as plt

def lorenz_system_with_euler(initial_conditions:dict, paramaters:dict):
    """
    Computes the solutions with explicit euler's method
    :param initial_conditions: Dictionary of initial conditions.
    :param paramaters: Dictionary of parameters.
    :return: x_solutions, y_solutions, z_solutions
    """

    # initial conditions and parameters
    x0, y0, z0 = [initial_conditions[key] for key in initial_conditions.keys()]
    sg, b, r, n, tt = [paramaters[key] for key in paramaters.keys()]

    # time sampling
    h = tt / n
    t = np.linspace(0, tt, n, endpoint=False)
    # t = np.arange(0,tt,h)

    # initializing solutions vectors
    x_solutions = np.zeros(t.size)
    y_solutions = np.zeros(t.size)
    z_solutions = np.zeros(t.size)

    # initializing solutions
    x_solutions[0] = x0
    y_solutions[0] = y0
    z_solutions[0] = z0

    # computing
    for i in range(1, t.size):
        x_solutions[i] = x_solutions[i-1] + h * sg * (y_solutions[i-1] - x_solutions[i-1])

        y_solutions[i] = y_solutions[i-1] + h * ( r * x_solutions[i-1] - y_solutions[i-1] - x_solutions[i-1] * z_solutions[i-1] )

        z_solutions[i] = z_solutions[i-1] + h * ( x_solutions[i-1] * y_solutions[i-1] - b * z_solutions[i-1] )

    return x_solutions, y_solutions, z_solutions

def plot_solutions(x_solutions:np.array, y_solutions:np.array, z_solutions:np.array, plot_name:str):
    """
    :param plot_name: Plot name
    :param x_solutions: Solutions on the x-axis.
    :param y_solutions: Solutions on the y-axis.
    :param z_solutions: Solutions on the z-axis.
    """
    fig = plt.figure(figsize=(10,9))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(x_solutions, y_solutions, z_solutions)
    plt.savefig(f"plots/{plot_name}.png")
    plt.close(fig)

def plot_comparison(vec1:np.array, vec2:np.array, vec1_label:str, vec2_label:str, plot_name:str):
    """
    :param vec2_label: Label for the second vector
    :param vec1_label: Label for the first vector
    :param vec1: 1st vector
    :param vec2: 2nd vector
    :param plot_name: Plot name
    :return:
    """
    t = np.linspace(0, 1, vec1.size, endpoint=False)
    plt.plot(t, vec1, label=vec1_label)
    plt.plot(t, vec2, label=vec2_label)
    plt.legend()
    plt.savefig(f"plots/{plot_name}.png")
    plt.close()