import streamlit as st
import numpy as np
import matplotlib.pyplot as plt


st.title("Projectile Motion Simulation 🚀")


v0 = st.number_input("Enter initial velocity (m/s):", min_value=1.0, value=20.0, step=1.0)
angle = st.number_input("Enter launch angle (degrees):", min_value=1.0, max_value=90.0, value=45.0, step=1.0)


g = 9.81  


theta = np.radians(angle)
t_flight = (2 * v0 * np.sin(theta)) / g
t = np.linspace(0, t_flight, num=100)
x = v0 * np.cos(theta) * t
y = v0 * np.sin(theta) * t - 0.5 * g * t**2


fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_xlabel("Horizontal Distance (m)")
ax.set_ylabel("Vertical Distance (m)")
ax.set_title("Projectile Motion Path")
ax.grid(True)


st.pyplot(fig)
