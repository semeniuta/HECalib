# -*- coding: utf-8 -*-

import olrem
import params
from classes.dataset import TCPCalibDataSet

datafile = params.datafiles[0]

ds = TCPCalibDataSet()
ds.read_file(datafile)

