# -*- coding: utf-8 -*-
import diffcalib
import params
from matplotlib import pyplot as plt
       
def create_histogram(data, nbins, hist_color):
    plt.figure()    
    plt.hist(data, nbins, color=hist_color)
    
if __name__ == '__main__':
    pairs, AB, res = diffcalib.read_and_process_pairs_for_different_calibrators(params.datafiles[0])
    
    res_pm = res[0]    
    
    create_histogram(res_pm['norms'], 100, 'blue')        
    create_histogram(res_pm['ratios'], 100, 'green') 