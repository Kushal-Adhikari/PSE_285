"""
Name : Kushal Adhikari
Date : 2026/09/10
Homework : 4

Objective: to find
Difference in force across a person near a black hole

Modules used: matplotlib.pyplot, numpy

Assumptions: The person is assumed to be standing radially, with the toes closer to the black hole than the head.

"""

import matplotlib.pyplot as plt
import numpy as np


def force_difference(radius: float | np.ndarray, black_hole_mass: float,
					 person_mass: float, body_length: float) -> float | np.ndarray:
	"""
	This function will calculate the tidal force difference across a person near a black hole.
	The person is assumed to be standing radially, with the toes closer to the black hole than the head.
	"""
	force_at_toes = Gravitational_constant * black_hole_mass * person_mass / radius**2
	force_at_head = (Gravitational_constant * black_hole_mass * person_mass
					 / (radius + body_length)**2)
	return force_at_toes - force_at_head


# Physical constants and typical values.
# Sources: https://physics.nist.gov/cgi-bin/cuu/Value?bg
#          https://ssd.jpl.nasa.gov/planets/phys_par.html

Gravitational_constant = 6.67430e-11   #  m^3 kg^-1 s^-2
SOLAR_MASS = 1.98847e30                # kg
EARTH_RADIUS = 6.371e6                 # m
SOLAR_RADIUS = 6.957e8                 # m
# Mass of my subject = 70.0            # kg
PERSON_MASS = 70.0                     # kg
# He is 1.70 m tall
BODY_LENGTH = 1.70                     # m
POUNDS_PER_NEWTON = 1 / 4.4482216152605

black_hole_mass = 1.0e6 * SOLAR_MASS     # Given in the problem

radii = np.geomspace(EARTH_RADIUS, SOLAR_RADIUS, 300)  #Returns number spaced evenly on a geometric progrssion


# Calling the force diff function
force_differences = force_difference(
	radii, black_hole_mass, PERSON_MASS, BODY_LENGTH
)


# Same thing here
earth_radius_difference = force_difference(
	EARTH_RADIUS, black_hole_mass, PERSON_MASS, BODY_LENGTH
)


# Same thing here
solar_radius_difference = force_difference(
	SOLAR_RADIUS, black_hole_mass, PERSON_MASS, BODY_LENGTH
)


# Printing the values in nice, organised and beautiful way
print(
	f"The force difference at one earth radius is "
	f"{earth_radius_difference:.3e} N "
	f"({earth_radius_difference * POUNDS_PER_NEWTON:.3e} pounds)."
)

print(
	f"The force difference at one solar radius is "
	f"{solar_radius_difference:.3e} N "
	f"({solar_radius_difference * POUNDS_PER_NEWTON:.3e} pounds)."
)


figure, axes = plt.subplots(figsize=(10, 6.5), dpi=120)
axes.set_facecolor("lightgray")
distance_in_earth_radii = radii / EARTH_RADIUS

# This is a geometric plot, so we use loglog to make it look better
axes.loglog(distance_in_earth_radii, force_differences, color= "blue",
            linewidth=3, label="Force difference")

# This  just plots the points for the force difference at one earth radius and one solar radius
axes.plot(1, earth_radius_difference, "o", color= "red", markersize=9,
          markeredgecolor="white", label="Earth distance") 

# same this for solar radius
axes.plot(SOLAR_RADIUS / EARTH_RADIUS, solar_radius_difference, "o",
          color= "green", markersize=9, markeredgecolor="white",
          label="Solar distance")
# labels
axes.set(xlabel="Distance from black hole center (Earth radii)",
         ylabel="Force difference between toes and head (N)",
         title="Tidal Force Across a Person Near a 1 Million Solar-Mass Black Hole")

# Beautification Stuff
axes.grid(True, which="both", color="gray", linestyle="--", alpha=0.7)
axes.legend(loc="upper right", facecolor="white")

# This prevents clipping
figure.tight_layout()
# This shows the plot
plt.show()
