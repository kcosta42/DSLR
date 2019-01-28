#!/Users/kcosta/.brew/bin/python3

from DSLR.core import load_csv, scatter_plot

import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
  dataset = load_csv('./datasets/dataset_train.csv')
  data = dataset[1:, :]
  data = data[data[:, 1].argsort()]

  X = np.array(data[:, 15], dtype=float)
  y = np.array(data[:, 16], dtype=float)
  legend = ['Grynffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin']

  scatter_plot(X, y, legend=legend, xlabel=dataset[0, 15], ylabel=dataset[0, 16])
