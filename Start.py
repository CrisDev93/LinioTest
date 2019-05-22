#!/usr/bin/env python
# -*- coding: utf-8 -*-


####################################
# File name: Start.py              #
# Author: Cristian Michel Zarate   #
# Date created: 22/05/2019         #
# Date last modified: 22/05/2019   #
# Python Version: 3.7.3            #
####################################

from Business import ModuloBusiness

business = ModuloBusiness.Modulo()

#Se usa un for para generar a serie de 1 al 100 e imprime el mensaje final
for number in range(1,101):
    response = business.calculateModulos(number)
    print("Number => " + str(number) + " " + response)
