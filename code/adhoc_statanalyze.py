# -*- coding: utf-8 -*-

import optandinit as oi
import params

if __name__ == '__main__':

    target = 'mean'    
    datafile = params.datafiles[2]
    
    norms_initial, norms_optimal, opt = oi.compare(datafile, target)
    
        
    
    

    
    
    
    
    