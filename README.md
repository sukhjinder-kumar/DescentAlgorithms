# Descent Algorithms

## Setup 

This is a webapp that shows Gradient descent and its variants via interactive examples.

To use this first clone the repo, then follow these steps -

1. Create a virtual environment (Recommended). And please note python3.9.7 seems to have some compatability issues with streamlit library. You can use python3.10 for instance. Example if you have venv installed, use `python3.10 -m venv <environment name>`

2. Install dependencies: `pip install -r requirements.txt` (Ensure you are in root directory of above code)

3. Run the app: `streamlit run index.py` 

## Documentation

- Input for the algorithms are given in the sidebar.

    1. Dimension: $F: \mathcal{R}^n \rightarrow \mathcal{R}$, here n is the dimension

    2. Function: User input function via text input. It is converted to python function using sympy library. One must note that python syntax for defining function must be used here.

    3. Intial Point: User input co-ordinates of intial point as `,` seprated numbers. Like `0, 1, 0`, it is converted to a numpy vector

    4. Number of iteration: It is always integer, currently min=1 and max=100.

    5. Step size: It is float with precision upto 2 decimals. Min=0.00 and max=1.00

- Each new algorithm has a seprate file in algorithm subfolder.
