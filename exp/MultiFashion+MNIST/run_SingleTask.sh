#seed=0
#name=SingleTask_T1
#task='T1'
#method='Baseline'
#
#CUDA_VISIBLE_DEVICES=1 python ./scripts/train_mnist.py --name $name --method $method --seed $seed --task $task

#python train_mnist.py --name SingleTask_T1 --method Baseline --seed 0 --task 'T1'
seed=0
name=SingleTask_T2
task='T2'
method='Baseline'

CUDA_VISIBLE_DEVICES=1 python train_mnist.py --name $name --method $method --seed $seed --task $task