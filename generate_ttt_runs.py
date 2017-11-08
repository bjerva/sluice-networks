#!/usr/bin/env python

'''
Generate experiment runs for Select or Reject
:author: Johannes Bjerva
'''

import argparse




base_slurm = '''#!/bin/bash
#SBATCH --job-name=TTT-{0}
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --time=6:00:00
#SBATCH --array=0-4
#SBATCH --partition=image1

'''

# parser = argparse.ArgumentParser()
# parser.add_argument('--n-runs', type=int, default=5)
# args = parser.parse_args()

base_python = '''python -u -O run_sluice_net.py --dynet-autobatch 1 --dynet-seed 123 --task-names pos --h-layers 1 --pred-layer 1  --patience 3 --train-dir ~/data/ --dev-dir ~/data/ --test-dir ~/data/ --train {0} --test {1} --constrain-matrices 0 --in-dim 1 --lemb-dir 081117/{0}_{1}_'''
log_dir = ' > ~/ttt_logs/$SLURM_ARRAY_TASK_ID/{0}_{1}.txt'

languages = 'UD_Finnish UD_Estonian UD_Hungarian UD_NorthSami'.split()

for l1 in languages:
    for l2 in languages:
        with open('ttt_runs/{0}_{1}.sh'.format(l1, l2), 'w') as out_f:
            out_f.write(base_slurm.format(l1+'_'+l2))
            out_f.write(base_python.format(l1, l2))
            out_f.write(log_dir.format(l1, l2))
