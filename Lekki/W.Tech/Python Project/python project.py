# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 00:12:16 2018

@author: ISAAC
"""

# USING PYTHON TO DRAW GRAPH OF SIMULTANEOUS EQUATION 

# NAME: IDOWU ISAAC OLUWAGBEMIGA
# EMAIL: idowu.isaaco@yahoo.com

''' PROJECT QUESTION 
Solve the following simultaneous equation graphically.

2x+3y=8
3x+2y=7
The coordinates of each graph is given below
2x+3y=8
x=[0,1,2,3,4,5], y=[8/3,2,4/3,2/3,0,-2/3]

3x+2y=7
x=[0,1,2,3,4,5], y=[3.5,2,0.5,-1,-2.5,-4]
'''
import matplotlib.pyplot as plt

plt.plot([0,1,2,3,4,5],[8/3,2,4/3,2/3,0,-2/3])
plt.plot([0,1,2,3,4,5],[3.5,2,0.5,-1,-2.5,-4])
plt.show
