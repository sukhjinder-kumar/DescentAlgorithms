import plotly.graph_objects as go
import numpy as np
import streamlit as st


def plot_plotly(history, func):

    fig = go.Figure()

    # Init points
    x_0 = history[0]
    r_lim = np.abs(2*x_0)+1  # Plus 1 to avoid error for 0
    l_lim = -r_lim
    num_pts = 4*int(r_lim)*10

    x_values = np.linspace(l_lim, r_lim, num_pts)
    # Rouding to 2 decimal else showing following error -
    # TypeError: Object of type Float is not JSON serializable
    y_values = np.array([
        "{:.2f}".format(func.subs({'x': x_val}).evalf())
        for x_val in x_values])

    # Plot function
    p1 = go.Scatter(x=x_values, y=y_values,
                    mode="lines")
    fig.add_trace(p1)

    # Plot History
    func_val = [
        "{:.2f}".format(func.subs({'x': x_val}).evalf())
        for x_val in history]
    history_ = ["{:.2f}".format(h) for h in history]
    p2 = go.Scatter(x=history_, y=func_val,
                    mode="lines")

    fig.add_trace(p2)

    st.plotly_chart(fig)
