import numpy as np
import math3d as m3d
from park_martin_calibration import ParkMartinCalibrator
from tsai_lenz_calibration import TsaiLenzCalibrator
from os.path import join as opj

datadir = r'../data'

calib = np.load(opj(datadir, '20131114121046.npy'))
newcalib1 = []
newcalib2 = []
newcalib3 = []
for x in calib:
    newcalib1.append((x[1],x[0]))

parkmartin = ParkMartinCalibrator()
  #set pose pairs and calculate move parameters
parkmartin.pose_pairs = calib
  # get transfrom martix between hand and eye

tsailenz = TsaiLenzCalibrator(calib)

park1 = parkmartin.sensor_in_flange
tzai1 = tsailenz.sensor_in_flange

parkmartin = ParkMartinCalibrator()
#set pose pairs and calculate move parameters
parkmartin.pose_pairs = newcalib1
# get transfrom martix between hand and eye
tsailenz = TsaiLenzCalibrator(newcalib1)

park2 = parkmartin.sensor_in_flange
tzai2 = tsailenz.sensor_in_flange



print "PARK:----------------------\n",park1, park2.inverse(), park2,park1.inverse()

print "TZAI:----------------------\n",tzai1, tzai2
