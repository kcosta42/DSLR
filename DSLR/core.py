# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    core.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kcosta <kcosta@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/01/28 11:35:15 by kcosta            #+#    #+#              #
#    Updated: 2019/01/28 18:20:55 by kcosta           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from DSLR.math import count_, mean_, std_, min_, max_, percentile_

import csv
import numpy as np
import matplotlib.pyplot as plt

def describe(filename):
  dataset = load_csv(filename)
  features = dataset[0]
  dataset = dataset[1:, :]
  print(f'{"":15} |{"Count":>12} |{"Mean":>12} |{"Std":>12} |{"Min":>12} |{"25%":>12} |{"50%":>12} |{"75%":>12} |{"Max":>12}')
  for i in range(0, len(features)):
    print(f'{features[i]:15.15}', end=' |')
    try:
      data = np.array(dataset[:, i], dtype=float)
      data = data[~np.isnan(data)]
      print(f'{count_(data):>12.4f}', end=' |')
      print(f'{mean_(data):>12.4f}', end=' |')
      print(f'{std_(data):>12.4f}', end=' |')
      print(f'{min_(data):>12.4f}', end=' |')
      print(f'{percentile_(data, 25):>12.4f}', end=' |')
      print(f'{percentile_(data, 50):>12.4f}', end=' |')
      print(f'{percentile_(data, 75):>12.4f}', end=' |')
      print(f'{max_(data):>12.4f}')
    except:
      print(f'{count_(dataset[:, i]):>12.4f}', end=' |')
      print(f'{"No numerical value to display":>60}')

def load_csv(filename):
  dataset = list()
  with open(filename) as csvfile:
    reader = csv.reader(csvfile)
    try:
      for _ in reader:
        row = list()
        for value in _:
          try:
            value = float(value)
          except:
            if not value:
              value = np.nan
          row.append(value)
        dataset.append(row)
    except csv.Error as e:
      print(f'file {filename}, line {reader.line_num}: {e}')
  return np.array(dataset, dtype=object)

def histogram(X, legend, title, xlabel, ylabel):
  plt.hist(X[:327], color='red', alpha=0.5)
  plt.hist(X[327:856], color='yellow', alpha=0.5)
  plt.hist(X[856:1299], color='blue', alpha=0.5)
  plt.hist(X[1299:], color='green', alpha=0.5)

  plt.legend(legend, loc='upper right')
  plt.title(title)
  plt.xlabel(xlabel)
  plt.ylabel(ylabel)
  plt.show()

def scatter_plot(X, y, legend, xlabel, ylabel):
  plt.scatter(X[:327], y[:327], color='red', alpha=0.5)
  plt.scatter(X[327:856], y[327:856], color='yellow', alpha=0.5)
  plt.scatter(X[856:1299], y[856:1299], color='blue', alpha=0.5)
  plt.scatter(X[1299:], y[1299:], color='green', alpha=0.5)

  plt.legend(legend, loc='upper right')
  plt.xlabel(xlabel)
  plt.ylabel(ylabel)
  plt.show()

def pair_plot_hist(ax, X):
  h1 = X[:327]
  h1 = h1[~np.isnan(h1)]
  ax.hist(h1, alpha=0.5)

  h2 = X[327:856]
  h2 = h2[~np.isnan(h2)]
  ax.hist(h2, alpha=0.5)

  h3 = X[856:1299]
  h3 = h3[~np.isnan(h3)]
  ax.hist(h3, alpha=0.5)

  h4 = X[1299:]
  h4 = h4[~np.isnan(h4)]
  ax.hist(h4, alpha=0.5)

def pair_plot_scatter(ax, X, y):
  ax.scatter(X[:327], y[:327], color='red', alpha=0.5)
  ax.scatter(X[327:856], y[327:856], color='yellow', alpha=0.5)
  ax.scatter(X[856:1299], y[856:1299], color='blue', alpha=0.5)
  ax.scatter(X[1299:], y[1299:], color='green', alpha=0.5)

def pair_plot(dataset, features, legend):
  size = 5 #dataset.shape[1]

  _, ax = plt.subplots(nrows=size, ncols=size, constrained_layout=True)
  for i in range(0, size):
    for j in range(0, size):
      X = dataset[:, i]
      y = dataset[:, j]
      if i == j:
        pair_plot_hist(ax[i, j], X)
      else:
        pair_plot_scatter(ax[i, j], X, y)
  plt.legend(legend)
  plt.show()
