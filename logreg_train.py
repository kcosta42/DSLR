#!/Users/kcosta/.brew/bin/python3

from DSLR.preprocessing import StandardScaler, train_test_split
from DSLR.model import LogisticRegression

from sklearn.metrics import accuracy_score

import pandas as pd
import numpy as np

if __name__ == '__main__':
  df = pd.read_csv('./datasets/dataset_train.csv')
  df = df.dropna(subset=['Defense Against the Dark Arts'])
  df = df.dropna(subset=['Charms'])
  df = df.dropna(subset=['Herbology'])
  df = df.dropna(subset=['Divination'])
  df = df.dropna(subset=['Muggle Studies'])
  X = np.array(df.values[1:, [9, 17, 8, 10, 11]], dtype=float)
  y = df.values[1:, 1]

  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

  sc = StandardScaler()
  sc.fit(X_train)

  X_train_std = sc.transform(X_train)
  X_test_std = sc.transform(X_test)

  lr = LogisticRegression(eta=0.1, max_iter=250)
  lr.fit(X_train_std, y_train)

  K = np.unique(y).tolist()

  y_pred = lr.predict(X_test_std)
  y_pred = [K[x] for x in y_pred]
  print(f'Misclasified samples: {sum(y_test != y_pred)}')
  print(f'Accuracy: {accuracy_score(y_test, y_pred):.2f}')
