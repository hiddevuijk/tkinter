import numpy as np
from sys import exit
from os import mkdir
from shutil import copy

TList = [1.1,1.2,1.3,1.325,1.35,1.4,1.5]
N = 500
navg = 60
dt = 0.00001
tf = 0.5
teq = 5
rho = 1./3.9
nbin = 500
seed = 123456789

program = 'go.exe'
dirnames = open('dirnames.txt','w')
for Ti, T in enumerate(TList):

		dirname = "T"+str(Ti)

		dirnames.write(dirname+'\n')
		mkdir(dirname)
		copy("../prog/"+program,dirname+'/'+program)
		name = ""
		infile = open(dirname+"/input.txt",'w')
		infile.write("N = %i \n" % N)
		infile.write("navg = %i \n" % navg)
		infile.write("seed = %i\n" % seed)
		infile.write("T = %f\n" % T)
		infile.write("dt= %1.15f\n" % dt)
		infile.write("tf= %f\n" % tf)
		infile.write("teq= %f\n" % teq)
		infile.write("rho = %f\n" % rho)
		infile.write("nbin= %i\n" % nbin)

		infile.close()


		runfile = open(dirname+"/run.sh",'w')
		runfile.write("#!/bin/bash\n")
		runfile.write("#SBATCH -J " + dirname+'\n')
		runfile.write("#SBATCH -n 1"+'\n')
		runfile.write("#SBATCH -e out.%J"+'\n')
		runfile.write("#SBATCH -o out.%j"+'\n')
		runfile.write("#SBATCH -p NODED"+'\n')
		runfile.write("time ./"+program+'\n')
		runfile.close()
dirnames.close()
