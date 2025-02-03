#!/bin/bash
N=1 # max number of parallel scripts allowed
True=1
False=0

export CUDA_MODULE_LOADING=LAZY

python cleanrl/ddpg_continuous_action.py --seed 1 \
    --env-id HalfCheetah-v4
    # --env-id CartPole-v1 \
    # --total-timesteps 200000 # 50000

# no more jobs to be started but wait for pending jobs
# (all need to be finished)
wait

echo "all done"