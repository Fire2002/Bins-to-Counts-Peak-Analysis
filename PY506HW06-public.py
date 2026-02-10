# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 08:55:59 2023

@author: MB
"""

# PY506 HW6 code

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# linear background fct: f(E_i) = m*E_i + b
# read data: PY506hw6-counts-data.txt

X = pd.read_csv('<insert path to data file here>',
                         sep = " ", header = None)
data = X[0]
bins = np.linspace(0, len(data)-1, len(data)) # bin array

def my_func(BlL, BlR, CL, CR, BuL, BuR):

    S = 0 # signal counts
    
    background_lower = 0 # lower background count
    background_upper = 0 # upper background count
    
    x_lower = 0 # lower bin
    x_upper = 0 # upper bin

    for i in range(BlL, BlR):
        
        background_lower += data[i]
        x_lower += i
        
    BLavg = background_lower/(np.abs(BlR - BlL))
    XLavg = x_lower/(np.abs(BlR - BlL))
    
    for j in range(BuL, BuR):
        
        background_upper += data[j]
        x_upper += j
        
    BUavg = background_upper/(np.abs(BuR - BuL))
    XUavg = x_upper/(np.abs(BuR - BuL))
    
    m = (BUavg - BLavg)/(XUavg - XLavg)
    b = BLavg
    best_fit = m*(bins - XLavg)+b
    
    #subtracting off background data:

    for k in range (CL, CR):
        
        S += (data[k] - best_fit[k])
    
    plt.close()
    plt.plot(bins, data, color = 'black', label='original data')
    plt.plot(bins, best_fit, color = 'red', label='background best fit line')
    plt.xlim(left = BlL - 10, right = BuR + 10)
    plt.xlabel('Bin count')
    plt.ylabel('Counts per Bins')
    plt.ylim(0,S/3)
    
    # left lines
    
    plt.axvline(BlL, ymax = data[BlL]/(S/3), color = 'blue')
    plt.axvline(BlR, ymax = data[BlR]/(S/3), color = 'blue')
    
    # center lines
    
    plt.axvline(CL, ymax = data[CL]/(S/3), color = 'green')
    plt.axvline(CR, ymax = data[CR]/(S/3), color = 'green')
    
    # right lines
    
    plt.axvline(BuL, ymax = data[BuL]/(S/3), color = 'purple')
    plt.axvline(BuR, ymax = data[BuR]/(S/3), color = 'purple')
    
    plt.title('Peak Analysis using fitted background for Bin {:f}'.format(0.5*(CL+CR)),fontsize=12)
    plt.legend()
    plt.show()

# analyzing peak in bin 140

def analyze_bin140():
    my_func(130,132,134,146,150,155)

# analyzing peak in bin 285

def analyze_bin285():
    my_func(274,276,277,293,295,300)

# analyzing peak in bin 520

def analyze_bin520():
    my_func(509,512,513,527,532,535)

analyze_bin140()
analyze_bin285()
analyze_bin520()







