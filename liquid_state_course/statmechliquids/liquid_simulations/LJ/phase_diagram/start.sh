#!/bin/bash

while read dirname
do
	cd /beetmp/hidde/LJ/phase_diagram/$dirname
	sbatch run.sh
done < dirnames.txt



