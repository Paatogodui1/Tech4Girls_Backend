#!/bin/bash

n=$1
Sum=0
for (( i=1 ; i<=n ; i++ )) 
do
Sum=$(($Sum+i))
done
echo "The sum of numbers from 1 to $n is:$Sum."
