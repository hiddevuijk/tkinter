import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sys import exit
def drawSphere(xCenter, yCenter, zCenter, r):
    #draw sphere
    u, v = np.mgrid[0:2*np.pi:10j, 0:np.pi:10j]
    x=np.cos(u)*np.sin(v)
    y=np.sin(u)*np.sin(v)
    z=np.cos(v)
    # shift and scale sphere
    x = r*x + xCenter
    y = r*y + yCenter
    z = r*z + zCenter
    return (x,y,z)

def snapshot(data,L):
    r= .5


    nsample = 100
    x,y,z = data[:,0],data[:,1],data[:,2]
    nskip = 1
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    for (xi,yi,zi) in zip(x,y,z):
        (xs,ys,zs) = drawSphere(xi,yi,zi,r)
        ax.plot_wireframe(xs, ys, zs,color=np.random.rand(3,))

    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")
    plt.xlim([0,L])
    plt.ylim([0,L])
    ax.set_zlim(0,L)
    plt.show()
data = np.loadtxt("config.dat",delimiter=';')
snapshot(data,10)
