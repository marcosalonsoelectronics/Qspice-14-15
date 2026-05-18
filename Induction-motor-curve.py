# -*- coding: utf-8 -*-
"""
Created on Thu May 24 12:13:02 2018

@author: Marcos Alonso
"""
import numpy as np
from   math import floor, log, sqrt, pi
import matplotlib.pyplot as plt
import cmath
j=(-1)**0.5
fe=60; we=2*pi*fe; V1=460/sqrt(3)

# Example 6.4 - Fitzgerald
R1=0.163; X1=0.793; X2=1.101; Xm=18.87; R2=0.5; Npp=2

L1=X1/(2*pi*fe); L2=X2/(2*pi*fe) ; Lm=Xm/(2*pi*fe)
print("L1(mH)=", L1*1000); print("L2(mH)=", L2*1000); print("Lm(mH)=", Lm*1000)

ws=we/Npp
Z1eq= j*Xm*(R1 + j*X1)/( R1 + j*(X1 + Xm) )
R1eq= Z1eq.real; X1eq= Z1eq.imag
V1eq= V1*Xm/sqrt(   R1**2 + (X1+Xm)**2 )

print("ws=", ws); print("ns=", ws*60/(2*pi))
print("Z1eq= ", Z1eq)
print("R1eq= ", R1eq); print("X1eq= ", X1eq)

def s(wm): 
    return  (ws - wm)/ws

def Te(wm): 
    return  (1/ws)*(3*V1eq**2*(R2/s(wm)))/( (R1eq + R2/s(wm))**2 + (X1eq + X2)**2  )

# print(Te(100))

Xmin= 0
Xmax= ws
Step= 0.1
Npoints = int((Xmax - Xmin)/Step)
print ("Npoints =", Npoints)

x = np.linspace(Xmin, Xmax, Npoints)
y = np.zeros_like(x)

for i in range (0, Npoints):
    y[i]  = Te(x[i])
    # print(x[i]*60/(2*pi), y[i])

    
# Representación de La
plt.figure(1)
plt.plot(x*60/(2*pi), y, 'red')
plt.grid(True)
plt.xlabel("Angular speed (rpm), $n_m$")
plt.ylabel("Torque, $T_e$")
plt.xlim(0,2000)
plt.ylim(0,300)
# plt.xticks(np.arange(0, 10, 1))
# plt.yticks(np.arange(0, 15, 2))
#plt.text(4, 14.6, "Mi función", size=14, backgroundcolor='white')
#plt.savefig("Mi_funcion.png", dpi=300)


