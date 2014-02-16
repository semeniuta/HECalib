# -*- coding: utf-8 -*-

import numpy as np
import math3d as m3d

def extract(orig):
    '''
    Extracts a matrix as a NumPy array
    from a math3d object
    '''
    rot_matrix = orig.matrix
    return np.array(rot_matrix)  