# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 15:00:45 2020

@author: davidbiton3
"""

from code_files import ACO
import sys


if __name__ == "__main__" :
    
    orig_stdout = sys.stdout
    f = open('out.txt', 'w')
    
    sys.stdout = f            # outpput write to the file directly.
          
    Niter = 100               # number of ligel iteration to find a soulition.
    Nant = 200                # number of ants every iteration.
    number_of_queens = 64     # number of queens to search.
    
    ant_colony = ACO.AntforNQueen(number_of_queens, Nant, Niter, rho = 0.05, alpha = 1, beta = 1.5)
    ant_colony.run()
    
    sys.stdout = orig_stdout
    f.close()