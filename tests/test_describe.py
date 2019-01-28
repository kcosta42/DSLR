# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test_describe.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kcosta <kcosta@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/01/28 11:56:57 by kcosta            #+#    #+#              #
#    Updated: 2019/01/28 13:50:01 by kcosta           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from DSLR.core import describe

def test():
  print('---------- Describe Test ----------')
  describe('./datasets/dataset_train.csv')
