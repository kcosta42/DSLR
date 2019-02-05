# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    model.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kcosta <kcosta@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/01/29 10:11:37 by kcosta            #+#    #+#              #
#    Updated: 2019/02/05 10:44:35 by kcosta           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np

class LogisticRegression(object):
  """Logistic Regression classifier

  Parameters
  ----------
  eta: float, default: 0.1
    Learning rate (between 0.0 and 1.0)
  max_iter: int, default: 50
    Max passes over the training dataset
  Lambda: float, default: 0
    Regularization term

  Attributes
  ----------
  _w: {array-like}, shape = [n_class, n_feature]
    Weights after fitting
  _errors: list
    Number of misclassifications in every epoch
  _cost: list
    Number of cost values
  """
  def __init__(self, eta=0.1, max_iter=50, Lambda=0, initial_weight=None, multi_class=None):
    self.eta = eta
    self.max_iter = max_iter
    self.Lambda = Lambda
    self._w = initial_weight
    self._K = multi_class
    self._errors = []
    self._cost = []

  def fit(self, X, y, sample_weight=None):
    """Fit training data

    Parameters
    ----------
    X: {array-like}, shape = [n_samples, n_features]
      Training vectors
    y: array-like, shape = [n_samples]
      Target values
    sample_weight: 1d-array, default: None
      Initial weights

    Return
    ------
    self: object
    """
    self._K = np.unique(y).tolist()
    newX = np.insert(X, 0, 1, axis=1)
    m = newX.shape[0]

    self._w = sample_weight
    if not self._w:
      self._w = np.zeros(newX.shape[1] * len(self._K))
    self._w = self._w.reshape(len(self._K), newX.shape[1])

    yVec = np.zeros((len(y), len(self._K)))
    for i in range(0, len(y)):
      yVec[i, self._K.index(y[i])] = 1

    for _ in range(0, self.max_iter):
      predictions = self.net_input(newX).T

      lhs = yVec.T.dot(np.log(predictions))
      rhs = (1 - yVec).T.dot(np.log(1 - predictions))

      r1 = (self.Lambda / (2 * m)) * sum(sum(self._w[:, 1:] ** 2))
      cost = (-1 / m) * sum(lhs + rhs) + r1
      self._cost.append(cost)
      self._errors.append(sum(y != self.predict(X)))

      r2 = (self.Lambda / m) * self._w[:, 1:]
      self._w = self._w - (self.eta * (1 / m) * (predictions - yVec).T.dot(newX) + np.insert(r2, 0, 0, axis=1))
    return self

  def net_input(self, X):
    return self.sigmoid(self._w.dot(X.T))

  def predict(self, X):
    X = np.insert(X, 0, 1, axis=1)
    predictions = self.net_input(X).T
    return [self._K[x] for x in predictions.argmax(1)]

  def save_model(self, sc, filename='./datasets/weights.csv'):
    f = open(filename, 'w+')

    for i in range(0, len(self._K)):
      f.write(f'{self._K[i]},')
    f.write('Mean,Std\n')

    for j in range(0, self._w.shape[1]):
      for i in range(0, self._w.shape[0]):
        f.write(f'{self._w[i][j]},')
      f.write(f'{sc._mean[j - 1] if j > 0 else ""},{sc._std[j - 1] if j > 0 else ""}\n')

    f.close()
    return self

  def sigmoid(self, z):
    g = 1.0 / (1.0 + np.exp(-z))
    return g
