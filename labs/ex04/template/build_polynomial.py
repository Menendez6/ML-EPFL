# -*- coding: utf-8 -*-
"""implement a polynomial basis function."""

import numpy as np


def build_poly(x, degree):
    """polynomial basis functions for input data x, for j=0 up to j=degree."""
    # ***************************************************
    # INSERT YOUR CODE HERE
    # polynomial basis function: TODO
    # this function should return the matrix formed
    # by applying the polynomial basis to the input data
    # ***************************************************
    output = np.ones((x.shape[0],1))
    for j in range(1,degree+1):
        x_new = np.power(x,j)
        x_new = x_new.reshape((x.shape[0],1))
        output = np.hstack((output,x_new))
    
    return output
    raise NotImplementedError

