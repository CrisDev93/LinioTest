#!/usr/bin/env python
# -*- coding: utf-8 -*-


####################################
# File name: ModuloModel.py     #
# Author: Cristian Michel Zarate   #
# Date created: 22/05/2019         #
# Date last modified: 22/05/2019   #
# Python Version: 3.7.3            #
####################################

'''
ModuloModel
    Esta clase es la encargada de contener los modulos precargados y los mensajes que se muestran.
'''
class ModuloModel:
    '''
    Los indices de los mensajes contienen las respuestas, para el caso del ultimo índice contiene un mensaje vacío
    que se muestra cuando el número a calcular en las operaciones no encontró que era multiplo de 3,5 o ambas.
    '''
    def __init__(self):
        self.modulos = None
        self.messages = ['Linio','IT','Linianos','']


    def createModulo(self):
        self.modulos = [0,0,0]
        return self.modulos
