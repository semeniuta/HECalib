# -*- coding: utf-8 -*-

'''
Perform optimization with different objectives
'''

import argparse
import olrem
from optimize import HandEyeOptimizer
import params
import math3d as m3d
from helpers import stats
import os
from os.path import join as opj
import cPickle as pickle

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()
    parser.add_argument('fnumber')
    args = parser.parse_args()
    
    targets = ['min', 'mean', 'max', 'var']
    
    datafile = params.datafiles[int(args.fnumber)]
    print 'Reading data file %s...' % datafile
    pairs, AB, AB_pairs = olrem.read_pairs_and_calc_AB(datafile)
     
    for t in targets:    
        print '\nCurrent target: %s' % t
        f = os.path.basename(datafile).split('.')[0]
        pickle_file = opj(params.datadir, 'opt_%s_%s.pickle' % (t, f))
        if os.path.exists(pickle_file):
            print 'Unpicking data...'
            with open(pickle_file, 'rb') as f: 
                opt = pickle.load(f)
        else:
            print 'Performing optimization...'
            opt = HandEyeOptimizer(pairs, AB)
            opt.minimization_target = t
            opt.perform_optimization(verbose=False)
            print 'Picking data...'
            with open(pickle_file, 'wb') as f:        
                pickle.dump(opt, f)
            
        XInititial = opt.XInitial
        XOptimal = opt.XOptimal
        
        to_m3d = lambda matrix: m3d.Transform(matrix)
        norms_initial = olrem.calc_norms(AB, to_m3d(XInititial), params.norm_func)    
        norms_optimal = olrem.calc_norms(AB, to_m3d(XOptimal), params.norm_func)
        
        stats.print_statistics_header()
        s_initial = stats.calc_statistics(norms_initial[1])
        s_optimal = stats.calc_statistics(norms_optimal[1])
        
        stats.print_statistics(s_initial)    
        stats.print_statistics(s_optimal)
        