#!/bin/bash
echo "What is your age?"
read Age 

if [[ "$Age" -lt 18 ]]
then 
 echo "You are a minor."
elif [[ "$Age" -ge 18 && "$Age" -le 64 ]]
then 
 echo "You are an adult."
else
 echo "You are a senior."
fi
