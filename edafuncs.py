"""Provides functions for exploratory data analysis."""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def eda_hist(data, col, labels):
    """Takes a DataFrame, column of interest, and list of labels,
    returns a histogram.
    """
    fig, ax = plt.subplots(figsize=(15, 5))
    sns.histplot(data=data, x=col, ax=ax)
    ax.set_xlabel(labels[1], fontdict={'fontsize':'x-large'})
    ax.set_ylabel('Count', fontdict={'fontsize':'x-large'})
    ax.set_title(labels[0], fontdict={'fontsize':'xx-large'})
    return fig, ax


def eda_kde(data, col, labels, hue=None):
    """Takes a DataFrame, column of interest, list of labels,
    and variable mapped to hue, returns a KDE plot.
    """
    fig, ax = plt.subplots(figsize=(15, 5))
    sns.kdeplot(data=data, x=col, hue=hue, ax=ax)
    ax.set_xlabel(labels[1], fontdict={'fontsize':'x-large'})
    ax.set_ylabel('Density', fontdict={'fontsize':'x-large'})
    ax.set_title(labels[0], fontdict={'fontsize':'xx-large'})
    return fig, ax


def tukey(data, col):
    """Takes a DataFrame and column of interest,
    returns the index of probable and possible outliers.
    """
    #Compute the IQR and inner and outer fences
    q1 = data[col].quantile(0.25)
    q3 = data[col].quantile(0.75)
    iqr = q3 - q1
    inner_fence = 1.5 * iqr
    outer_fence = 3 * iqr

    #Compute inner fence lower and upper ends
    inner_fence_lower = q1 - inner_fence
    inner_fence_upper = q3 + inner_fence

    #Compute outer fence lower and upper ends
    outer_fence_lower = q1 - outer_fence
    outer_fence_upper = q3 + outer_fence

    #If value is an outlier, append the index to the appropriate outlier list
    outliers_prob = []
    outliers_poss = []
    for index, x in enumerate(data[col]):
        if x <= outer_fence_lower or x >= outer_fence_upper:
            outliers_prob.append(index)
        elif x <= inner_fence_lower or x >= inner_fence_upper:
            outliers_poss.append(index)
    return pd.Series(outliers_prob), pd.Series(outliers_poss)
