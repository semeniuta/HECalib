# -*- coding: utf-8 -*-

import numpy as np

def np_norm(AX, XB):
    M = AX - XB    
    return np.linalg.norm(M)    
    
def max_abs(AX, XB):
    M = AX - XB
    return np.max(np.abs(M))

def m3d_distance(AX, XB):
    '''
    Calculate distance and angle among the two transforms AX and XB
    XB.orient.ang_dist(AX.orient)
    XB.pos.dist(AX.pos)
    '''
    return XB.pos.dist(AX.pos)