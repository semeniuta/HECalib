# -*- coding: utf-8 -*-

import olrem
import params

datafile = params.datafiles[0]

pairs = olrem.read_pairs(datafile)
AB = olrem.calc_AB(pairs)
