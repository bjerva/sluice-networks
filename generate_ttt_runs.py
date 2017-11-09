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

base_python = '''python -u -O run_sluice_net.py --dynet-autobatch 1 --task-names pos --h-layers 1 --pred-layer 1  --patience 3 --train-dir ~/data/ --dev-dir ~/data/ --test-dir ~/data/ --train {0} --test {1} --constrain-matrices 0 --in-dim 1 --model-dir ./models/{2}_{1}_$SLURM_ARRAY_TASK_ID_nolemb --log-dir ./logs/ --lemb-dir 081117/{2}_{1}_$SLURM_ARRAY_TASK_ID_nolemb'''
log_dir = ' > ~/ttt_logs/$SLURM_ARRAY_TASK_ID/{0}_{1}.txt'

languages = 'UD_Finnish UD_Estonian UD_Hungarian UD_NorthSami'.split()

for l1 in languages:
    for l2 in languages:
        with open('ttt_runs/{0}_{1}_nolemb.sh'.format(l1, l2), 'w') as out_f:
            out_f.write(base_slurm.format(l1[3:6]+'_'+l2[3:6]))
            out_f.write(base_python.format(l1, l2, l1))
            out_f.write(log_dir.format(l1, l2))

for l1 in languages:
    for l2 in languages:
        if l1 == l2: continue
        for l3 in languages:
            with open('ttt_runs/{0}_{1}_{2}_nolemb.sh'.format(l1, l2, l3), 'w') as out_f:
                out_f.write(base_slurm.format(l1[3:6]+'_'+l3[3:6]))
                out_f.write(base_python.format(l1+' '+l2, l3, l1+'_'+l2))
                out_f.write(log_dir.format(l1+'_'+l2, l3))


for l1 in languages:
    for l2 in languages:
        if l1 == l2: continue
        for l3 in languages:
            if l1 == l3 or l2 == l3: continue
            for l4 in languages:
                with open('ttt_runs/{0}_{1}_{2}_{3}_nolemb.sh'.format(l1, l2, l3, l4), 'w') as out_f:
                    out_f.write(base_slurm.format(l1[3:6]+'_'+l4[3:6]))
                    out_f.write(base_python.format(l1+' '+l2+' '+l3, l4, l1+'_'+l2+'_'+l3))
                    out_f.write(log_dir.format(l1+'_'+l2+'_'+l3, l4))
