# -*- coding: utf-8 -*-

'''
Interaction with ParkMartinCalibrator object
'''

def get_calibration_result(pairs, CalibratorClass):
    '''
    Get the result of hand-eye calibration (X matrix)
    using the given calibration class
    '''
    calibrator = CalibratorClass(pairs)
    return calibrator.sensor_in_flange
    
def extract_AB(calibrator_object):
    '''
    Extract (A, B) pairs from a ParkMartinCalibrator object
    '''
    AB = [(p1.move, p2.move) for p1, p2 in calibrator_object._move_pairs]
    return AB