import itertools
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def plot_pareto_front(data, title):
    fig, axs = plt.subplots(figsize=(7, 5))
    axs.scatter(data['rental'].to_numpy(),
                data['sale'].to_numpy(), color='blue')
    plt.suptitle(title)
    fig.tight_layout()
    axs.set_xlabel("Rent price")
    axs.set_ylabel("Sale price")
    return fig, axs

def plot_input_distributions(data):
    inputs = ['sqfeet',
              'beds',
              'baths',
              'income',
              'density']
    points = list(itertools.combinations(inputs, r=2))
    points = filter(lambda x: x[0]!= x[1], points)
    fig,axs = plt.subplots(2,5,figsize=(25,10))
    for i, (in1, in2) in enumerate(points):
        x, y = i//2, i % 2
        axs[y,x].scatter(x=data[in1], y=data[in2])
        axs[y,x].set_xlabel(in1)
        axs[y,x].set_ylabel(in2)
    plt.tight_layout()
    return fig, axs