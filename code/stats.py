# -*- coding: utf-8 -*-

import numpy as np

def calc_statistics(sample):
    res = {}
    res['mean'] = np.mean(sample)
    res['min'] = min(sample)
    res['max'] = max(sample)
    res['var'] = np.var(sample)
    res['stdev'] = np.std(sample)
    
    return res
    
def print_statistics(s):
    tpl = (s['min'], s['mean'], s['max'], s['var'], s['stdev'])
    print '%.2f\t%.2f\t%.2f\t%.2f\t%.2f' % tpl
    
def print_statistics_header():
    print 'min\tmean\tmax\tvar\tstdev'