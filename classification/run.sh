#!/bin/bash
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --gres=gpu:4 -c4
#SBATCH --time=04:00:00
#SBATCH --mem=160GB
#SBATCH --job-name=imgClassifier
#SBATCH --mail-type=END
#SBATCH --mail-user=jx603@nyu.edu
#SBATCH --output=slurm_%j.out

module purge
module load keras/2.0.2 

cd /scratch/jx603/operation-criminal-kitty/classification/

python train.py