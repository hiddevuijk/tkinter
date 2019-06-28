#!/bin/bash

while read dirname
do
	cd /beetmp/hidde/LJco/critPY/$dirname
	sbatch run.sh
done < dirnames.txt



