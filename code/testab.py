# -*- coding: utf-8 -*-

import params
import olrem
from park_martin_calibration import ParkMartinCalibrator

pairs, AB, AB_pairs = olrem.read_pairs_and_calc_AB(params.pairs_datafile, olrem.calc_AB_ML)
pm = ParkMartinCalibrator(pairs)    
AB_MortenLind = [(p1.move, p2.move) for p1, p2 in pm._move_pairs]

print AB[0]
print AB_MortenLind[0]

for i in range(len(AB)):
    print AB[i] == AB_MortenLind[i]