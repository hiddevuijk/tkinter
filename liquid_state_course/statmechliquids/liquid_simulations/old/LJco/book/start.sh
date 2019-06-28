#!/bin/bash

while read dirname
do
	cd /beetmp/hidde/LJco/book/$dirname
	sbatch run.sh
done < dirnames.txt



