#!/Users/kcosta/.brew/bin/python3

from DSLR.core import load_csv, pair_plot

import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
  dataset = load_csv('./datasets/dataset_train.csv')
  data = dataset[1:, 6:]
  data = data[data[:, 1].argsort()]

  features = dataset[0, 6:]
  legend = ['Grynffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin']

  pair_plot(np.array(data, dtype=float), features, legend)
  plt.show()
