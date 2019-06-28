import numpy as np

from py_solution import *
from potentials import *

class NumInt:
    def __init__(self):
        # system parameters
        self.HS = False
        self.rho = 0.85
        self.T = 1.
        self.r_co = 2.**(1./6.)

        # integration parameters
        self.a = 0.5
        self.R = 50.
        self.Nexp = 14
        self.N = -1+2**self.Nexp
        self.eps_conv = 1.e-6
        self.use_prev = False

        self.print_every = 25

        self.dr = 0
        self.r = 0
        self.k = 0
        self.f = 0
        self.kD = 0
        self.rc = 0
        self.kC = 0
        self.m = 0
        self.rd = 0

        self.eps = 0
        self.it = 0

    def init_vectors(self):
        self.it = 0
        self.eps = 10
        self.dr = self.R/(self.N-1)
        self.r = np.linspace(self.dr, self.R+self.dr,self.N)
        self.k = np.linspace(np.pi/self.R, np.pi*self.N/self.R,self.N)
        if self.use_prev == True:
            self.rd = np.loadtxt("name")
            if len(self.rd) is not self.N:
                return False
        else:
            self.rd = np.zeros(self.N)

        if self.HS == True:
            self.f = get_f_hs(self.r)
        else:
            self.f = get_f_LJ(self.T, self.r, self.r_co)

        self.kD = np.zeros(self.N)
        self.rc = np.zeros(self.N)
        self.kC = np.zeros(self.N)
        self.m = np.zeros(self.N)

        return True

    def iterate(self):
        self.rc = rd2rc(self.f, self.rd, self.r)
        self.kC = rc2kC(self.rc, self.r, self.N)
        self.kD = kC2kD(self.kC, self.k, self.rho)
        self.m = kD2rd(self.kD, self.r, self.N)

        self.eps = eps(self.rd, self.m)
        self.rd = self.a*self.rd + (1-self.a)*self.m

        self.it += 1
        
        
