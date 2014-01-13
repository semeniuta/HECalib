# -*- coding: utf-8 -*-

import diffcalib

if __name__ == '__main__':
    results = {}   
    for f in params.datafiles:
        pairs, AB, res = diffcalib.read_and_process_pairs_for_different_calibrators(f)   
        fname = os.path.basename(f)        
        results[fname] = res 
               
        print 'Results of processing data from %s' % fname
        print res[0]['X']
        print res[1]['X']
        
#        resprocess.print_res(res)
#        r_pm, r_tl = resprocess.sort_by_ratios(res)
#        print r_pm
#        print r_tl