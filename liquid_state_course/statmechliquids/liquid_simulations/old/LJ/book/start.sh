#!/bin/bash

while read dirname
do
	cd /beetmp/hidde/LJ/book/$dirname
	sbatch run.sh
done < dirnames.txt



