#!/usr/bin/python
import numpy as np
import sys
import pdb
import matplotlib.pyplot as plt

def main(argv):
    try:
        trajectory = np.loadtxt(argv[0])
    except:
        pass

    plt.plot(trajectory[:,1],'-*')
    plt.plot(trajectory[:,2],'-*')
    plt.plot(trajectory[:,3],'-*')
    plt.show()


if __name__ == '__main__':
    main(sys.argv[1:])
