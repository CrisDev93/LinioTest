#!/usr/bin/env python
# -*- coding: utf-8 -*-


####################################
# File name: ModulosControl.py     #
# Author: Cristian Michel Zarate   #
# Date created: 22/05/2019         #
# Date last modified: 22/05/2019   #
# Python Version: 3.7.3            #
####################################

'''
Control
    Esta clase es la encargada de hacer los calculos y decisión necesarias para obtener la respuesta correcta
    ante los datos de entradas.
'''
class Control:

    '''
    indexMessage
        Este método es encargado de decidir cual es el índice correcto que contiene el mensaje
        que se mostrará al final.

        @param data, modulos que contiene el resultado del los multiplos de 3 y 5 dado el número que
        proporcionó
        @return index, entero que el índice elegido, que puede ser 0,1 o 2 o en su defecto 3 cuando
        no es ni multiplo de 3 ni de 5 ni ambos.
    '''
    def indexMessage(self,data):
        index = 3
        for d in range(len(data)):
            if data[d] == 0:
                index = d
        return index

    '''
    calculateModulos
        Este método es encargado de setear los datos en los índices, cada indice contiene la información
        del resultado que es el multiplo tanto de 3 y 5, y en el ultimo índice colocar la suma del indice 1 y el indice 2.

        @param modules, modulos que contiene los datos precreados (en ceros)
        @param number, entero que contiene el numero elegido para realizar los calculos
        @return modules, modulos con la información del resultado de las operaciones realizadas.
    '''
    def calculateModulos(self,modules,number):
        modules[0] = number % 3
        modules[1] = number % 5
        modules[2] = modules[0] + modules[1]
        return modules
