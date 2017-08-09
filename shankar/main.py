#!/usr/bin/python
import numpy as np
import sys
import pdb
import matplotlib.pyplot as plt
import h5py


def print_attrs(name, obj):
    print(name)
    for key, val in obj.attrs.iteritems():
        print("    %s: %s" % (key, val))


data = h5py.File("cycles_high_7200.hdf5", "r")
data.visititems(print_attrs)

states = data['i_state']
time = data['time']

plt.plot(time, states[:,0],'-r')
plt.plot(states[:,1],'-g')
plt.plot(states[:,2],'-b')

# SLAM initial frame to inertial
R = np.matrix('1 0 0; 0 0 1; 0 -1 0')

trajectory = np.loadtxt('KeyFrameTrajectory.txt')
trajectory = trajectory[:, 1:4].T

time = np.linspace(0, time[-1], trajectory.shape[1])
trajectory = R * trajectory

# scale trajectory
scale = max(states[:,0])/max(trajectory[0].T)
trajectory = float(scale) * trajectory

# apply initial translation
trajectory = np.expand_dims(states[0, 0:3], axis=1) + trajectory

plt.plot(time, trajectory[0,:].T,'-*r')
plt.plot(time, trajectory[1,:].T,'-*g')
plt.plot(time, trajectory[2,:].T,'-*b')
plt.show()

plt.show()
