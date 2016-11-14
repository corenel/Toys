from __future__ import print_function
from scipy.io import loadmat
import matplotlib.pyplot as plt
import numpy as np
import sys
from os import path, listdir


def plot_data(filepath):
    matfile = loadmat(filepath)
    matdata = [matfile[x] for x in matfile if type(matfile[x]) is np.ndarray]
    plt.style.use('ggplot')
    for data in matdata:
        plt.figure()
        plt.ylabel('Y')
        plt.xlabel('X')
        for i in range(1, data.shape[1]):
            plt.plot(data[:, 0], data[:, i])
        plt.savefig('%s.png' % str(filepath).split('.')[0])
        plt.clf()
    # Specific configuration
    # for data in matdata:
    #     plt.figure()
    #     plt.ylabel('Level (cm)')
    #     plt.xlabel('Time (second)')
    #     t = data[:, 0]
    #     y1 = data[:, 1]
    #     y2 = data[:, 2]
    #     y3 = data[:, 3]
    #     plt.plot(t, y1, label='real plant', linewidth=2)
    #     plt.plot(t, y3, label='simualtion')
    #     plt.plot(t, y2, label='set value')
    #     plt.ylim(10, 20)
    #     plt.legend(loc=4)
    #     plt.savefig('%s.png' % str(filepath).split('.')[0])


if __name__ == '__main__':
    # argv
    if len(sys.argv) == 2 and path.exists(sys.argv[1]):
        datapath = sys.argv[1]
    else:
        print('Usage:\n    %s <file path> or <directory path>' % sys.argv[0])
        sys.exit(1)

    # file or directory
    if path.isfile(datapath):
        print('Ploting %s' % datapath)
        plot_data(datapath)
    elif path.isdir(datapath):
        filelist = [x for x in listdir(datapath) if path.splitext(x)[1] == '.mat']
        for datafile in filelist:
            print('Ploting %s' % datafile)
            plot_data('%s/%s' % (datapath, datafile))
