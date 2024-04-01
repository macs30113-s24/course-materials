#!/bin/bash
#SBATCH --job-name=cupy_pi   # job name
#SBATCH --output=cupy_pi.out # output log file
#SBATCH --time=00:05:00      # 5 minutes of wall time
#SBATCH --partition=gpu      # GPU partition
#SBATCH --nodes=1            # 1 GPU node
#SBATCH --ntasks=1           # 1 CPU core to drive GPU
#SBATCH --gres=gpu:1         # Request 1 GPU
#SBATCH --account=macs30113

module load cuda python

python3 cupy_gpu_pi.py
