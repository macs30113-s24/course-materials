#!/bin/bash
#SBATCH --job-name=cupy_rand_walk
#SBATCH --output=cupy_rand_walk.out
#SBATCH --time=00:05:00
#SBATCH --nodes=1
#SBATCH --partition=gpu
#SBATCH --ntasks=1
#SBATCH --gres=gpu:1
#SBATCH --account=macs30113
#SBATCH --mem-per-cpu=30G

module load python cuda

python3 cupy_rand_walk.py
