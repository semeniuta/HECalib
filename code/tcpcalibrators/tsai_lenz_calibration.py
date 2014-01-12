'''
Module for hand eye calibration

References: R.Tsai, R.K.Lenz "A new Technique for Fully Autonomous
            and Efficient 3D Robotics Hand/Eye calibration", IEEE
            trans. on robotics and Automaion, Vol.5, No.3, June 1989
'''

__author__ = 'Lars Tingelstad'
__email__ = 'lars.tingelstad@ntnu.no'

import numpy as np
import math3d as m3d

def skew(v):
    if len(v) == 4: v = v[:3]/v[3]
    skv = np.roll(np.roll(np.diag(v.flatten()), 1, 1), -1, 0)
    return skv - skv.T

def quat_to_rot(q):
    '''
    % quat2rot - a unit quaternion(3x1) to converts a rotation matrix (3x3)
    %
    %    R = quat2rot(q)
    %
    %    q - 3x1 unit quaternion
    %    R - 4x4 homogeneous rotation matrix (translation component is zero)
    %        q = sin(theta/2) * v
    %        teta - rotation angle
    %        v    - unit rotation axis, |v| = 1
    %
    % See also: rot2quat, rotx, roty, rotz, transl, rotvec

    function R = quat2rot(q)

        p = q'*q
    if( p > 1 ),
        disp('Warning: quat2rot: quaternion greater than 1');
    end
    w = sqrt(1 - p);                   % w = cos(theta/2)

    R = eye(4);
    R(1:3,1:3) = 2*q*q' + 2*w*skew(q) + eye(3) - 2*diag([p p p]);

    return
    '''
    q = np.array(q).reshape(3,1)
    p = np.dot(q.T,q).reshape(1)[0]
    if p > 1:
        print('Warning: quaternion greater than 1')
    w = np.sqrt(1 - p)
    R = np.eye(4)
    R[:3,:3] = 2*q*q.T + 2*w*skew(q) + np.eye(3) - 2*np.diag([p,p,p])
    return R

def rot_to_quat(r):
    '''
    % rot2quat - converts a rotation matrix (3x3) to a unit quaternion(3x1)
    %
    %    q = rot2quat(R)
    %
    %    R - 3x3 rotation matrix, or 4x4 homogeneous matrix
    %    q - 3x1 unit quaternion
    %        q = sin(theta/2) * v
    %        teta - rotation angle
    %        v    - unit rotation axis, |v| = 1
    %
    %
    % See also: quat2rot, rotx, roty, rotz, transl, rotvec

    function q = rot2quat(R)

        w4 = 2*sqrt( 1 + trace(R(1:3,1:3)) ); % can this be imaginary?
        q = [
            ( R(3,2) - R(2,3) ) / w4;
            ( R(1,3) - R(3,1) ) / w4;
        ( R(2,1) - R(1,2) ) / w4;
    ];
    return

    '''
    w4 = 2 * np.sqrt(1 - np.trace(r[:3,:3]))
    q = np.array([(r[2,1] - r[1,2]) / w4,
                  (r[0,2] - r[2,0]) / w4,
                  (r[1,0] - r[0,1]) / w4])
    return q

class TsaiLenzCalibrator(object):

    def __init__(self, pose_pairs=None):
        self.pose_pairs = pose_pairs

    def _solve(self):

        # // Calculate rotational component

        pp = self.pose_pairs
        M = len(pp)
        lhs = []
        rhs = []
        for i in range(M):
            for j in range(i+1,M):
                Hgij = pp[j][0].inverse() * pp[i][0]
                Pgij = 2 * Hgij.orient.quaternion.vector_part
                Hcij = pp[j][1].inverse() * pp[i][1]
                Pcij = 2 * Hcij.orient.quaternion.vector_part
                lhs.append(skew(Pgij.data + Pcij.data))
                rhs.append(Pcij.data - Pgij.data)
        lhs = np.array(lhs)
        lhs = lhs.reshape(lhs.shape[0]*3, 3)
        rhs = np.array(rhs)
        rhs = rhs.reshape(rhs.shape[0]*3)
        Pcg_, res, rank, sing = np.linalg.lstsq(lhs, rhs)
        Pcg = 2 * Pcg_ / np.sqrt(1 + np.dot(Pcg_.reshape(3), Pcg_.reshape(3)))
        Rcg = quat_to_rot(Pcg / 2)

        # // Calculate translational component
        lhs = []
        rhs = []
        for i in range(M):
            for j in range(i+1,M):
                Hgij = pp[j][0].inverse() * pp[i][0]
                Hcij = pp[j][1].inverse() * pp[i][1]
                lhs.append(Hgij.data[:3,:3] - np.eye(3))
                rhs.append(np.dot(Rcg[:3,:3], Hcij.pos.data) - Hgij.pos.data)
        lhs = np.array(lhs)
        lhs = lhs.reshape(lhs.shape[0]*3, 3)
        rhs = np.array(rhs)
        rhs = rhs.reshape(rhs.shape[0]*3)
        Tcg, res, rank, sing = np.linalg.lstsq(lhs, rhs)
        Hcg = m3d.Transform(np.ravel(Rcg[:3,:3]), Tcg)
        self._sif = Hcg

    @property
    def sensor_in_flange(self):
        self._solve()
        return self._sif


if __name__ == '__main__':
    pp = np.load('park_martin_test_pose_pairs.npy')
    tlc = TsaiLenzCalibrator(pp[:10])
    sif_tsai = tlc.sif

