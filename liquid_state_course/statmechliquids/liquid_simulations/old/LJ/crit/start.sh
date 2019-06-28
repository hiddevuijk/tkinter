#!/bin/bash

while read dirname
do
	cd /beetmp/hidde/LJ/crit/$dirname
	sbatch run.sh
done < dirnames.txt



