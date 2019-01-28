# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    setup.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kcosta <kcosta@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/01/28 11:35:23 by kcosta            #+#    #+#              #
#    Updated: 2019/01/28 11:35:26 by kcosta           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from setuptools import setup, find_packages

with open('README.md') as f:
  readme = f.read()

setup(
  name='DSLR',
  version='0.1',
  description=readme,
  author='kcosta',
  author_email='kcosta@student.42.fr',
  url='https://github.com/kcosta42/DSLR',
  license='MIT',
  packages=find_packages(exclude=('tests', 'docs'))
)
