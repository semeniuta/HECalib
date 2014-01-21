# -*- coding: utf-8 -*-

from tcpcalibrators.park_martin2 import ParkMartinCalibrator
import params
import olrem

dfile = params.datafiles[0]
pose_pairs = olrem.read_pairs(dfile)

pmc = ParkMartinCalibrator(pose_pairs)

