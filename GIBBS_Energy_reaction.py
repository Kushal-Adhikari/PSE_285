# Gmix = RT(xA  * ln xA + xB * ln xB)
# A does not mix with B during the reaction the energy changes linearly 



import numpy as np
import math 
import matplotlib.pyplot as plt

# Given Information
G_A = 10**(3.0)   #Joules/ mole
G_B = 2*10**(4.0)   #Joules/ mole
T = 300   #Kelvin
R = 8.314   #Joules/ mole-Kelvin


plt.title("Gibbs Energy of Reaction vs Mole Fraction")
plt.plot(np.linspace(0,1,100) , np.linspace(G_A, G_B, 100), label = "Gibbs Energy", color = "red")

plt.xlabel("Mole Fraction")
plt.ylabel("Gibbs Energy (J/mol)")
plt.legend()

Mix_List = []

# When it is mixing 
for x in np.linspace(0.001,0.999,100):
    G_mix = R * T * (x * math.log(x) + (1-x) * math.log(1-x))
    Mix_List.append(G_mix)

G_Total = np.linspace(G_A, G_B, 100) + Mix_List

plt.plot(np.linspace(0,1,100) , G_Total, label = "G_Total", color = "green")
plt.plot(np.linspace(0,1,100) , Mix_List, label = "G_Mix", color = "blue")
plt.legend()
plt.show()




