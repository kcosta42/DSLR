#!/Users/kcosta/.brew/bin/python3

from DSLR.core import load_csv, histogram

import numpy as np

if __name__ == '__main__':
  dataset = load_csv('./datasets/dataset_train.csv')
  data = dataset[1:, :]
  data = data[data[:, 1].argsort()]

  X = np.array(data[:, 16], dtype=float)
  legend = ['Grynffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin']

  histogram(X, legend=legend, title=dataset[0, 16], xlabel='Marks', ylabel='Number of student')
