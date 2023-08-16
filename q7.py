# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 08:12:26 2023

@author: joaod
"""

import math
import numpy as np
import numpy.random as npr

def questao_7():
     
    a8 = np.array([[1,2,3],[0,5,0],[7,8,9]])
    iden = np.identity(3)
    determ = np.linalg.det(a8)
    
    # se tudo estiver certo, então AA^(-1)=I
    inv = np.linalg.inv(a8)
    resultado = np.matmul(a8, inv)
    resultado = np.round(resultado, 0)
    print(resultado) #que é o determinante!
    
questao_7()
    
