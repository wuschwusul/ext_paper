#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Falcor
#
# Created:     14.02.2015
# Copyright:   (c) Falcor 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import numpy as np
import random as rnd

def main():
    prob=0.05
    species=100

    cij= get_c(prob)
    x=init_x(species)


    pass


def get_c(prob,species):   #returns  Cij in unity for given Probability and Nr of Species
    cij=np.zeros(species,species)

    for i,row in enumerate(cij):
        for j,col in enumerate(row):
            zz =rnd.randint(0,100)/100
            if zz<prob:
                cij(i,j)=1
            else:
                cij(i,j)=0

    return cij


def init_x(spc):
    for i in range(spc):
        for j in range(spc):
            x_delta.... HIER WEITER ij
            for k in range(spc):
                x_delta=x_delta+ .. HIER AUCH kj



if __name__ == '__main__':
    main()
