# -*- coding: utf-8 -*-

import diffcalib
import olrem
import params

pairs, AB, res = diffcalib.process_pairs_for_different_calibrators()

cal1, cal2 = res
n = len(cal1['norms'])
for i in range(n):
    print i, cal1['norms'][i], cal2['norms'][i]

criterion = olrem.create_filtering_criterion(params.filtering_top_limit)
fi = olrem.filter_pairs(pairs, res[0]['norms'], criterion)
print fi