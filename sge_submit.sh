#$ -cwd
#$ -o $JOB_ID-$TASK_ID.o
#$ -e $JOB_ID-$TASK_ID.e

# enter the virtual environment


if [ $SGE_TASK_ID -eq 1]
   then python3 search_parameter.py --run_id $JOB_ID --nic_name eth0 --working_dir .
else
   python3 search_parameter.py --run_id $JOB_ID --nic_name eth0  --working_dir . --worker
fi
