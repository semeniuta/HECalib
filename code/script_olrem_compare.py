# -*- coding: utf-8 -*-

import params
from outliers.distang import DistAngOutliersEliminator
from outliers.norms import NormsOutliersEliminator

if __name__ == '__main__':
    datafile = params.datafiles[0]
    
    noe = NormsOutliersEliminator(datafile)
    doe = DistAngOutliersEliminator(datafile)
    
    n = noe.old_norms
    d = doe.old_distances
    
    

