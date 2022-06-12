"""Provides functions for running bootstrap hypothesis tests."""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def bs_replicates(data, func, n=1, seed=0):
    """Takes an array of data, function, number of replicates, and random seed,
    resamples data n times with replacement and uses func to compute and
    return array of bootstrap test statistics."""
    np.random.seed(seed)
    replicates = [func(np.random.choice(data, len(data))) for i in range(n)]
    return replicates


def jellybean_hist(data, labels):
    """Takes an array of data and list of labels,
    returns a histogram with 95% confidence interval shaded in grey.
    """
    fig, ax = plt.subplots(figsize=(15, 5))
    sns.histplot(data=data, ax=ax)
    ax.set_xlabel(labels[1], fontdict={'fontsize':'x-large'})
    ax.set_ylabel('Count', fontdict={'fontsize':'x-large'})
    ax.set_title(labels[0], fontdict={'fontsize':'xx-large'})

    #Mark 95% confidence interval in gray
    lower, upper = np.percentile(data, [2.5, 97.5])
    plt.axvspan(lower, upper, color='grey', alpha=0.2)
    return fig, ax

def equal_tail_p_value(data, observed_stat):
    """Takes an array of data and an observed test statistic,
    prints the equal-tail p-value of the data against the test statistic.
    """
    p = 2 * np.minimum(np.sum(data <= observed_stat)/5000,
                       np.sum(data > observed_stat)/5000)
    print('p-value =', p)


def print_95_ci(data):
    """Takes an array of data, prints 95% confidence interval."""
    lower, upper = np.percentile(data, [2.5, 97.5])
    print(f'95% Confidence Interval: {lower}, {upper}')
