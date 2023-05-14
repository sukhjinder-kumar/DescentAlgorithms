import streamlit as st
import numpy as np
import sympy
#from matplotlib import pyplot as plt

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
dim = st.sidebar.number_input(
    "1. Enter dimension of function's domain (default = 1)",
    value=1)

# Input function definition
func_str = st.sidebar.text_input(
        "2. Enter function (in python format, like x**3 + sin(x)): ",
        value="x**2")
func = sympy.sympify(func_str)
# st.sidebar.write(func.subs({'x': 2}).evalf())

# Input intial point
def_int_point =  ("0," * dim)[:-1]
intial_point = st.sidebar.text_input(
        "3. Enter intial point where each coord is , seprated: ",
        value=def_int_point)
x_0 = np.array(tuple(intial_point.split(",")), dtype=float).reshape(dim, 1)

# Input number of iterations
num_iter = st.sidebar.slider(
    "4. Enter Number of iteration of algorithm: ",
    value=10,
    min_value=1,
    max_value=100)

# Input step size
step_size = st.sidebar.slider(
        "5. Select step_size: ",
        value=1.0)

##############################################
# Algorithms
##############################################

algo_list = ["GradientDescent"]

algo = st.selectbox(
        "Select a Descent algorithm: ",
        options=algo_list,
        index=0)

# TODO
# 1. Create a general function def for Algorithms.
# What to take input, what to output
# 2. Figure out how to import and export those functions
# 3. Visualization for 1, and 2-Dimensional spaces.
# Idealy with points on the surface of function and a nice
# animation showing movement of the points.
