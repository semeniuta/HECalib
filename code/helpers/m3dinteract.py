# -*- coding: utf-8 -*-

import numpy as np
import pandas

def extract(orig):
    '''
    Extracts a matrix as a NumPy array
    from a math3d object
    '''
    rot_matrix = orig.matrix
    return np.array(rot_matrix)  

def flatten_transform(t):
    orient = np.array(t.orient.matrix).flatten()
    pos = np.array(t.pos.matrix).flatten()
    return np.hstack((orient, pos))

def get_transfom_dataframe(list_of_transforms):
    pass