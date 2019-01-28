# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kcosta <kcosta@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/01/28 11:23:11 by kcosta            #+#    #+#              #
#    Updated: 2019/01/28 11:24:57 by kcosta           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

NAME := DSLR

.PHONY: install test clean

install:
	@python3 -m pip install -r requirements.txt

test:
	@python3 setup.py test || true

clean:
	@python3 setup.py clean
	@rm -rf $(NAME)/__pycache__/	2> /dev/null || true
	@rm -rf tests/__pycache__/		2> /dev/null || true
	@rm -rf $(NAME).egg-info/ 		2> /dev/null || true
