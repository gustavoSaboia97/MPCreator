#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Descricao          : Start the modules
# AUTOR              : Gustavo Saboia
# DATA               : 22/08/2018
#-------------------------------------------------------------------------------------
from Classes.Parameter import Parameter
import sys

parameter = Parameter()
parameter.get_parameters(sys.argv)
parameter.run_application()