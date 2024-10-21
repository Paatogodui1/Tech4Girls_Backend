#!/bin/bash
Number=20
while [[ $Number -gt 0 ]]
do 
 echo "$Number"
Number=$(($Number-1))
done
 echo "Countdown complete!"