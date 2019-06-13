#!/bin/bash
#$ -N sge_test_job
#$ -o /home/lchen/sge_log/sge_stdout_logs/
#$ -e /home/lchen/sge_log/sge_stderr_logs/

# enter the virtual environment
source /home/lchen/parameters/parameter/bin/activate

if [ $SGE_TASK_ID -eq 1]
   then python3 /home/lchen/parameters/search_parameter.py --run_id $JOB_ID --nic_name lo 
else
   python3 /home/lchen/parameters/search_parameter.py --run_id $JOB_ID --nic_name lo --worker
fi
