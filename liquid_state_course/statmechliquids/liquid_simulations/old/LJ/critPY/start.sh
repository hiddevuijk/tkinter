#!/bin/bash

while read dirname
do
	cd /beetmp/hidde/LJ/critPY/$dirname
	sbatch run.sh
done < dirnames.txt



