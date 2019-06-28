#!/bin/bash

while read dirname
do
	cd /beetmp/hidde/LJco/liquid/$dirname
	sbatch run.sh
done < dirnames.txt



