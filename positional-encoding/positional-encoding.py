import numpy as np

def positional_encoding(seq_len, d_model, base=10000.0):
    """
    Return PE of shape (seq_len, d_model) using sin/cos formulation.
    Odd d_model -> last column is sin.
    """
    # Write code here
    pass

    # Create placeholder matrix of zeros.
    pe = np.zeros((seq_len, d_model))

    # Create the position vectors
    # Shape: (seq_len, 1)
    # Add np.newaxis to turn the flat array of length T into a shape of (T, 1)
    pos = np.arange(seq_len)[:, np.newaxis]

    # Calculate the divisor (frequencies)
    # Create an array of even indices for 
    i_even = np.arange(0, d_model, 2)
    div_term = np.exp(i_even * -(np.log(base) / d_model))

    # Calculate the angles
    angles = pos * div_term

    # Fill the Matrix in 
    pe[:, 0::2] = np.sin(angles)

    # Use angles[:, :d_model//2] to ensure shapes match if d_model is odd
    pe[:, 1::2] = np.cos(angles[:, :d_model//2])

    return pe
    