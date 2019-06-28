#!/bin/bash

while read dirname
do
	cd /beetmp/hidde/LJco/gas/$dirname
	sbatch run.sh
done < dirnames.txt



