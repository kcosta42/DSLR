# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    preprocessing.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kcosta <kcosta@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/01/29 10:22:50 by kcosta            #+#    #+#              #
#    Updated: 2019/01/31 14:10:36 by kcosta           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from DSLR.math import mean_, std_
import numpy as np

def train_test_split(X, y, test_size=0.3, random_state=None):
  """Split arrays or matrices into random train and test subsets

  Parameters
  ----------
  X : array-like, shape [n_samples, n_features]
  y: array-like, shape = [n_samples]
  test_size: float, default: 0.3
  random_state: int, default: 0
  """
  if random_state:
    np.random.seed(random_state)

  p = np.random.permutation(len(X))

  X_offset = int(len(X) * test_size)
  y_offset = int(len(y) * test_size)

  X_train = X[p][X_offset:]
  X_test = X[p][:X_offset]

  y_train = y[p][y_offset:]
  y_test = y[p][:y_offset]
  return (X_train, X_test, y_train, y_test)

class StandardScaler(object):
  """Standardize features by removing the mean and scaling to unit variance

  Attributes
  ----------
  _mean: 1d-array, shape [n_features]
    Mean of the training samples or zero
  _std: 1d-array, shape [n_features]
    Standard deviation of the training samples or one
  """
  def __init__(self, mean=np.array([]), std=np.array([])):
    self._mean = mean
    self._std = std

  def fit(self, X):
    """Compute the mean and std to be used for later scaling.

    Parameters
    ----------
    X : array-like, shape [n_samples, n_features]
    """
    for i in range(0, X.shape[1]):
      self._mean = np.append(self._mean, mean_(X[:, i]))
      self._std = np.append(self._std, std_(X[:, i]))

  def transform(self, X):
    """Perform standardization by centering and scaling

    Parameters
    ----------
    X : array-like, shape [n_samples, n_features]
    """
    return ((X - self._mean) / self._std)
