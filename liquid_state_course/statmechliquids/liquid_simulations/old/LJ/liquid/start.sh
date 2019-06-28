#!/bin/bash

while read dirname
do
	cd /beetmp/hidde/LJ/liquid/$dirname
	sbatch run.sh
done < dirnames.txt



