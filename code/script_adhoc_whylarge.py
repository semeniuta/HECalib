# -*- coding: utf-8 -*-

''' 
Test the results of matrices multiplication and subtractions
using numpy arrays and math3d.Transfrom objects
'''

import params
import olrem
from hecalibrators import calibinteract as ci
from helpers import m3dinteract as m3di

CalibratorClass = params.calibrator_classes[0]
pairs, AB, AB_pairs = olrem.read_pairs_and_calc_AB(params.datafiles[0])
X = ci.get_calibration_result(pairs, CalibratorClass)

A, B = AB[0]

Z1 = A*X
Z2 = X*B

z1 = m3di.extract(Z1)
z2 = m3di.extract(Z2)
z = z1-z2

''' ======================================================================= '''

a = m3di.extract(A)
b = m3di.extract(B)
x = m3di.extract(X)

z_np = a*x - x*b




