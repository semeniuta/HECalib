# -*- coding: utf-8 -*-

''' 
Test the results of matrices multiplication and subtractions
using numpy arrays and math3d.Transfrom objects
'''

import params
import olrem

CalibratorClass = params.calibrator_classes[0]
pairs, AB = olrem.read_pairs_and_calc_AB(params.pairs_datafile)
X = olrem.get_calibration_result(pairs, CalibratorClass)

A, B = AB[0]

Z1 = A*X
Z2 = X*B

z1 = olrem.extract(Z1)
z2 = olrem.extract(Z2)
z = z1-z2

''' ======================================================================= '''

a = olrem.extract(A)
b = olrem.extract(B)
x = olrem.extract(X)

z_np = a*x - x*b




