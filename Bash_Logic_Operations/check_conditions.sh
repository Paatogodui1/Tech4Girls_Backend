#!/bin/bash
Number1=$1
Nunmber2=$2

if (( $1 -gt 10 && $2 -gt 10 ))
then 
echo "Both numbers are greater than 1o"
elif (( $1 -gt 10 || $2 -gt 10 ))
echo "At least one number is greater than 10" 
else
echo "Neither number is greater than 10"
fi