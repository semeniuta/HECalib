# -*- coding: utf-8 -*-

import olrem
from optimize import HandEyeOptimizer
import params
from matplotlib import pyplot as plt
import math3d as m3d
import stats
import os
from os.path import join as opj
import cPickle as pickle

if __name__ == '__main__':

    print 'Reading data files...'
    datafile = params.datafiles[0]
    pairs, AB, AB_pairs = olrem.read_pairs_and_calc_AB(datafile, calc_AB_func=olrem.calc_AB_ML)
    
    pickle_file = opj(params.datadir, 'opt_mean.pickle')
    
    if os.path.exists(pickle_file):
        print 'Unpicking data...'
        with open(pickle_file, 'rb') as f: 
            opt1 = pickle.load(f)
    else:
        print 'Performing optimization...'
        opt1 = HandEyeOptimizer(pairs, AB)
        opt1.perform_optimization(verbose=False)
        print 'Picking data...'
        with open(pickle_file, 'wb') as f:        
            pickle.dump(opt1, f)
        
    XInititial = opt1.XInitial
    XOptimal = opt1.XOptimal

    print XInititial
    print XOptimal
    
    to_m3d = lambda matrix: m3d.Transform(matrix)
    norms_initial = olrem.calc_norms(AB, XInititial, params.norm_func)    
    norms_optimal = olrem.calc_norms(AB, XOptimal, params.norm_func)
    
    s_initial = stats.calc_statistics(norms_initial[1])
    s_optimal = stats.calc_statistics(norms_optimal[1])
    
    stats.print_statistics_header()
    stats.print_statistics(s_initial)    
    stats.print_statistics(s_optimal)
    
    plt.figure()
    plt.xlabel('Values of ||AX-XB|| norms')
    plt.ylabel('Frequency')
    plt.hist(norms_initial[1], 100, color="gray", label='Original X')
    plt.hist(norms_optimal[1], 100, color="green", label='Optimized X')
    plt.legend(('Original X', 'Optimized X'))
    
    
    