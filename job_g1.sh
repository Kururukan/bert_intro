#!/bin/tcsh
#PBS -l nodes=1:ppn=4:metideep-G1
#PBS -q default
#PBS -j oe
#PBS -o stdout
#PBS -e stdout
#PBS -N openai


cd $PBS_O_WORKDIR
set path =($path /usr/local/bin)
set path =($path /home/username/.local)

# pipenv shell error

python3 posi_nega.py

hostname