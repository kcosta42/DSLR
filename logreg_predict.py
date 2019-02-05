#!/Users/kcosta/.brew/bin/python3

from DSLR.preprocessing import StandardScaler
from DSLR.model import LogisticRegression

from sklearn.metrics import accuracy_score

import argparse

import pandas as pd
import numpy as np

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument("dataset", type=str, help="input dataset")
  parser.add_argument("weights", type=str, help="input weights")
  args = parser.parse_args()

  df = pd.read_csv(args.dataset)
  df = df.fillna(method='ffill')
  X = np.array(df.values[:, [9, 17, 8, 10, 11]], dtype=float)

  df = pd.read_csv(args.weights)
  K = list(df)[:4]
  mean = df.values[1:, 4]
  std = df.values[1:, 5]
  weights = df.values[:, :4].T

  sc = StandardScaler(mean, std)
  X_std = sc.transform(X)

  lr = LogisticRegression(initial_weight=weights,multi_class=K)

  y_pred = lr.predict(X_std)

  f = open("houses.csv", 'w+')
  f.write('Index,Hogwarts House\n')
  for i in range(0, len(y_pred)):
    f.write(f'{i},{y_pred[i]}\n')

