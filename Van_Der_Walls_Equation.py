# given equation : (P + a(n/V)^2)(V - nb) = nRT

# Temp Range  0 to 100 C
# i.e 273 373 K

# Moles n = 2
import numpy as np
import matplotlib.pyplot as plt


Volume = 1.0 # liters
Moles = 2.0 # moles
Temp = np.linspace(273, 373, 100) # Kelvin
R = 0.0821 # L atm / K mol

a_for_Oxygen = 1.36 # L^2 atm / mol^2
b_for_Oxygen = 0.0318 # L / mol

a_for_Nitrogen = 1.39 # L^2 atm / mol^2
b_for_Nitrogen = 0.0391 # L / mol

a_for_Krypton = 2.32 # L^2 atm / mol^2
b_for_Krypton = 0.0266 # L / mol

a_for_Hexane = 2.25 # L^2 atm / mol^2
b_for_Hexane = 0.0638 # L / mol



def calculate_pressure(a, b, V, n, T):

    return (n * R * T) / (V - n * b) - a * (n / V)**2

Ideal_Pressure = (Moles * R * Temp) / Volume

plt.title("Pressure vs Temperature for Different Gases")
plt.plot(Temp, Ideal_Pressure, label = "Ideal", color = "black")
plt.plot(Temp, calculate_pressure(a_for_Oxygen, b_for_Oxygen, Volume, Moles, Temp), label = "Oxygen", color = "blue")
plt.plot(Temp, calculate_pressure(a_for_Nitrogen, b_for_Nitrogen, Volume, Moles, Temp), label = "Nitrogen", color = "green")
plt.plot(Temp, calculate_pressure(a_for_Krypton, b_for_Krypton, Volume, Moles, Temp), label = "Krypton", color = "red")
plt.plot(Temp, calculate_pressure(a_for_Hexane, b_for_Hexane, Volume, Moles, Temp), label = "Hexane", color = "orange")
plt.xlabel("Temperature (K)")   
plt.ylabel("Pressure (atm)")
plt.legend()

plt.margins(0, 0)
plt.show()