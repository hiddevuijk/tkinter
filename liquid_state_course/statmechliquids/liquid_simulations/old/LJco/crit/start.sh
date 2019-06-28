#!/bin/bash

while read dirname
do
	cd /beetmp/hidde/LJco/crit/$dirname
	sbatch run.sh
done < dirnames.txt



