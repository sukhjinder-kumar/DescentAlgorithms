import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits import mplot3d
import streamlit as st


def plot_matplotlib_2D(history, func):
    # Config
    x_0 = history[0]
    r_lim = np.abs(2*x_0)+1  # Plus 1 to avoid error for 0
    l_lim = -r_lim

    num_pts = 4*int(r_lim)*10
    x_values = np.linspace(l_lim, r_lim, num_pts)
    y_values = np.array([
        func.subs({'x': x_val}).evalf() for x_val in x_values])

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


def plot_matplotlib_3D(history, func):
    fig = plt.figure()
    ax = plt.axes(projection='3d')

    # Config
    X_0 = history[0]
    x = X_0[0][0]
    y = X_0[1][0]

    # e,w,n,s stands for east, west, north, south
    xs_lim = np.abs(2*x)+1  # Plus 1 to avoid error for 0
    xn_lim = -xs_lim
    ye_lim = np.abs(2*y)+1
    yw_lim = -ye_lim

    xnum_pts = int(xs_lim)*10
    ynum_pts = int(ye_lim)*10

    x_values = np.linspace(xn_lim, xs_lim, xnum_pts)
    y_values = np.linspace(yw_lim, ye_lim, ynum_pts)
    X, Y = np.meshgrid(x_values, y_values)
    Z = np.zeros([ynum_pts, xnum_pts])

    zmin = np.inf
    zmax = -np.inf
    for i in range(0, ynum_pts):
        for j in range(0, xnum_pts):
            Z[i][j] = (func.subs({'x': X[i][j], 'y': Y[i][j]}).evalf())
            if Z[i][j] < zmin:
                zmin = Z[i][j]
            if Z[i][j] > zmax:
                zmax = Z[i][j]

    # Plot History
    x_val = [float(X[0][0]) for X in history]
    y_val = [float(X[1][0]) for X in history]
    z_val = [func.subs({'x': x, 'y': y}).evalf() for x, y in zip(x_val, y_val)]

    ax.plot3D(x_val, y_val, z_val, color='black', label="iterates")
    fig.legend()

    # Plotting function
    ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
                    cmap='viridis', edgecolor='none')
    ax.set_xlim3d(xn_lim, xs_lim)
    ax.set_ylim3d(yw_lim, ye_lim)
    ax.set_zlim3d(zmin, zmax)
    ax.set_xlabel('x-axis')
    ax.set_ylabel('y-axis')
    ax.set_zlabel('F')
    ax.set_title(f"{func}")

    st.pyplot(fig)
