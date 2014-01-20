# -*- coding: utf-8 -*-

class TCPCalibration:
    def __init__(self, dataset, CalibratorClass):
        self.dataset = dataset
        self.calibrator = CalibratorClass(dataset.positions)
        
    def get_calibration_result(self):
        return self.calibrator.sensor_in_flange