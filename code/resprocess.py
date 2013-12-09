# -*- coding: utf-8 -*-

'''
Process the results of olrem.process_pairs function
'''

def print_res(res):
    print 'Number\tPark-Martin\tTsai-Lenz\tRatio(PM)\tRatio(TL)'
    cal1, cal2 = res
    n = len(cal1['norms'])
    for i in range(n):
        print '%d\t%.2f\t%.2f\t%.2f\t%.2f' % (i, cal1['norms'][i], cal2['norms'][i], cal1['ratios'][i], cal2['ratios'][i])
    print 'Means of ratios (PM, TL): %.2f, %.2f' % (cal1['ratios_mean'], cal2['ratios_mean'])
    print 'Stdevs of ratios (PM, TL): %.2f, %.2f' % (cal1['ratios_stdev'], cal1['ratios_stdev'])
        
def sort_by_ratios(res):
    cal1, cal2 = res
    take_val = lambda x: x[1]
    take_ind = lambda x: x[0]
    norms_1 = [(i, cal1['norms'][i]) for i in range(len(cal1['norms']))]
    norms_2 = [(i, cal2['norms'][i]) for i in range(len(cal2['norms']))]
    s1 = sorted(norms_1, key=take_val)
    s2 = sorted(norms_2, key=take_val)
    indices_1 = [take_ind(tpl) for tpl in s1]
    indices_2 = [take_ind(tpl) for tpl in s2]  
    
    take_first_10 = lambda x: x[:25]
    
    first_AB_pairs_1 = [(ind, cal1['AB_pairs'][ind], cal1['norms'][ind]) for ind in indices_1]
    first_AB_pairs_2 = [(ind, cal2['AB_pairs'][ind], cal2['norms'][ind]) for ind in indices_2]
        
    return first_AB_pairs_1, first_AB_pairs_2