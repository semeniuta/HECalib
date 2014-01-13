# -*- coding: utf-8 -*-

import optimize
import olrem
import params

if __name__ == '__main__':
    
    ''' Open data file and calculate X matrix using ParkMartinCalibrator '''
    datafile = params.datafiles[0]
    pairs, AB, AB_pairs = olrem.read_pairs_and_calc_AB(datafile)
    opt = optimize.HandEyeOptimizer(pairs, AB)
    opt.perform_optimization(verbose=False)