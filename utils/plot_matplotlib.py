import numpy as np
from matplotlib import pyplot as plt
import streamlit as st


def plot_matplotlib(history, func):
    # Function plot
    x_0 = history[0]
    r_lim = np.abs(2*x_0)+1  # Plus 1 to avoid error for 0
    l_lim = -r_lim

    num_pts = 4*int(r_lim)*10
    x_values = np.linspace(l_lim, r_lim, num_pts)
    y_values = np.array([
        func.subs({'x': x_val}).evalf() for x_val in x_values])
    print(x_values)
    print(y_values)

    # Matplotlib implementation
    fig, ax = plt.subplots()
    ax.set_xlim(l_lim, r_lim)
    ax.set_ylim(bottom=float(np.amin(y_values)), top=float(np.amax(y_values)))
    ax.plot(x_values, y_values, color="black")
    ax.set_title(f"{func}")
    ax.set_xlabel("x-axis")
    ax.set_ylabel("F(x)")

    # History plot
    func_val = np.array([
        func.subs({'x': x_val}).evalf() for x_val in history])
    ax.plot(history, func_val, color="blue", label="Iterates")
    ax.legend()

    st.pyplot(fig)
