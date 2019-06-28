#!/bin/bash

while read dirname
do
	cd /beetmp/hidde/LJ/gas/$dirname
	sbatch run.sh
done < dirnames.txt



