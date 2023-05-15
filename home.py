import streamlit as st
import numpy as np
import sympy

from algorithms.gradientdescent import GD
from utils.plot_matplotlib import plot_matplotlib
from utils.plot_plotly import plot_plotly

st.set_page_config(
        page_title = "DescentAlgorithms",
        page_icon = "./assets/img/GD1.png",)

st.write("# Descent Algorithms")
st.divider()

##############################################
# Input Parameters
##############################################

st.sidebar.write("## Input")

# Input dimension of domain of function
n = st.sidebar.radio(
    "1. Enter dimension of function's domain (default = 1)",
    ("1", "2"),
    horizontal=True,
    index=0)
dim = int(n)

# Input function definition
func_str = st.sidebar.text_input(
        "2. Enter function (in python format, like x\*\*3 + sin(x) \
                or x\*\*2 + y\*\*2): ",
        value="x**2")
func = sympy.sympify(func_str)
# st.sidebar.write(func.subs({'x': 2}).evalf())

# Input intial point
def_int_point =  ("0," * dim)[:-1]
intial_point = st.sidebar.text_input(
        "3. Enter intial point where each coord is , seprated: ",
        value=def_int_point)
x_0 = np.array(tuple(intial_point.split(",")), dtype=float).reshape(dim, 1)
if dim == 1:
    x_0 = float(x_0)

# Input number of iterations
num_iter = st.sidebar.slider(
    "4. Enter Number of iteration of algorithm: ",
    value=10,
    min_value=1,
    max_value=100)

# Input step size
step_size = st.sidebar.slider(
        "5. Select step_size: ",
        value=1.0,
        min_value=0.0,
        max_value=2.0,
        step=0.01)


##############################################
# Algorithms
##############################################

algo_list = ["GradientDescent"]

algo = st.selectbox(
        "Select a Descent algorithm: ",
        options=algo_list,
        index=0)

if algo == "GradientDescent":
    history = GD(dim, func, x_0, num_iter, step_size)
else:
    st.write("Under developement")

##############################################
# Plotting
##############################################

# Note - Viz is quite bad, a feature to zoom and
# focus is essential. Ig plotly has that feature

if st.checkbox("Show raw history"):
    st.write(history)

if dim == 1:
    plot_matplotlib(history, func)
    plot_plotly(history, func)
else:
    st.write("In progress")

# TODO
# Visualization for 1, and 2-Dimensional spaces.
# Idealy with points on the surface of function and a nice
# animation showing movement of the points.
