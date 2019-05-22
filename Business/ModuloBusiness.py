#!/usr/bin/env python
# -*- coding: utf-8 -*-


####################################
# File name: ModuloBusiness.py     #
# Author: Cristian Michel Zarate   #
# Date created: 22/05/2019         #
# Date last modified: 22/05/2019   #
# Python Version: 3.7.3            #
####################################


from Model import ModuloModel
from Control import ModulosControl

'''
Modulo
    Esta clase es la encargada de hacer los llamados a todos los metodos necesarios para obtener
    la respuesta adecuada.
'''
class Modulo:

    def __init__(self):
        self.modulosModel = ModuloModel.ModuloModel()
        self.core = ModulosControl.Control()
    '''
    calculateModulos
        Este método es encargado de hacer el llamado al controlador para realizar los calculos
        necesarios, enviarle el arreglo de los modulos precreados y elegir la respuesta correcta.

        @param number, entero elegido para realizar la operación.
        @return string, cadena que contiene la respuesta final a mostrar.
    '''
    def calculateModulos(self,number):
        modules = self.modulosModel.createModulo()
        modules = self.core.calculateModulos(modules,number)
        indexSelected = self.core.indexMessage(modules)
        return self.modulosModel.messages[indexSelected]
