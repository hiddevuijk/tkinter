#!/bin/bash
#SBATCH -J T4
#SBATCH -n 1
#SBATCH -e out.%J
#SBATCH -o out.%j
#SBATCH -p NODED
time ./go.exe
