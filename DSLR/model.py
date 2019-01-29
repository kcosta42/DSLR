# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    model.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kcosta <kcosta@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/01/29 10:11:37 by kcosta            #+#    #+#              #
#    Updated: 2019/01/29 14:14:39 by kcosta           ###   ########.fr        #
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

  Attributes
  ----------
  _w: {array-like}, shape = [n_class, n_feature]
    Weights after fitting
  _errors: list
    Number of misclassifications in every epoch
  _cost: list
    Number of cost values
  """
  def __init__(self, eta=0.1, max_iter=50):
    self.eta = eta
    self.max_iter = max_iter

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
    K = np.unique(y).tolist()
    X = np.insert(X, 0, 1, axis=1)
    m = X.shape[0]

    self._w = sample_weight
    if not self._w:
      self._w = np.zeros(X.shape[1] * len(K))
    self._w = self._w.reshape(len(K), X.shape[1])

    yVec = np.zeros((len(y), len(K)))
    for i in range(0, len(y)):
      yVec[i, K.index(y[i])] = 1

    for _ in range(0, self.max_iter):
      predictions = self.net_input(X).T - yVec
      self._w = self._w - self.eta * (1 / m) * predictions.T.dot(X)
    return self

  def net_input(self, X):
    return self.sigmoid(self._w.dot(X.T))

  def predict(self, X):
    X = np.insert(X, 0, 1, axis=1)
    predictions = self.net_input(X).T
    return predictions.argmax(1)

  def sigmoid(self, z):
    g = 1.0 / (1.0 + np.exp(-z))
    return g
