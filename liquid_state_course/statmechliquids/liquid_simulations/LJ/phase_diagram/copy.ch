#!/bin/bash

while read dirname
do
	cp $dirname/P.dat "../../data/LJ/"$dirname"_p.dat"
done < dirnames.txt



