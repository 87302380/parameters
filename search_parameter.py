import logging
logging.basicConfig(level=logging.WARNING)
import os
import pickle
import time

import argparse

import hpbandster.core.nameserver as hpns

from hpbandster.optimizers import BOHB as BOHB
from testWorker import testWorker as worker

parser = argparse.ArgumentParser(description='Example 1 - sequential and local execution.')
parser.add_argument('--min_budget',   type=float, help='Minimum budget used during the optimization.',    default=9)
parser.add_argument('--max_budget',   type=float, help='Maximum budget used during the optimization.',    default=243)
parser.add_argument('--n_iterations', type=int,   help='Number of iterations performed by the optimizer', default=10)
parser.add_argument('--n_workers', type=int,   help='Number of workers to run in parallel.', default=2)
parser.add_argument('--worker', help='Flag to turn this into a worker process', action='store_true')
parser.add_argument('--run_id', type=str, help='A unique run id for this optimization run. An easy option is to use the job id of the clusters scheduler.')
parser.add_argument('--nic_name',type=str, help='Which network interface to use for communication.')
parser.add_argument('--shared_directory',type=str, help='A directory that is accessible for all processes, e.g. a NFS share.', default='/home/lchen/parameters/result')

args=parser.parse_args()

host = hpns.nic_name_to_host(args.nic_name)


if args.worker:

    time.sleep(5)   # short artificial delay to make sure the nameserver is already running
    w = worker(sleep_interval = 0.5,run_id=args.run_id, host=host)
    w.load_nameserver_credentials(working_directory=args.shared_directory)
    w.run(background=False)
    exit(0)

result_logger = hpres.json_result_logger(directory=args.shared_directory, overwrite=True)


# Step 1: Start a nameserver
# Every run needs a nameserver. It could be a 'static' server with a
# permanent address, but here it will be started for the local machine with the default port.
# The nameserver manages the concurrent running workers across all possible threads or clusternodes.
# Note the run_id argument. This uniquely identifies a run of any HpBandSter optimizer.
NS = hpns.NameServer(run_id=args.run_id, host=host, port=0, working_directory=args.shared_directory)
ns_host, ns_port = NS.start()

# Step 2: Start a worker
# Now we can instantiate a worker, providing the mandatory information
# Besides the sleep_interval, we need to define the nameserver information and
# the same run_id as above. After that, we can start the worker in the background,
# where it will wait for incoming configurations to evaluate.
w = worker(sleep_interval = 0.5,run_id=args.run_id, host=host, nameserver=ns_host, nameserver_port=ns_port)
w.run(background=True)

# Step 3: Run an optimizer
# Now we can create an optimizer object and start the run.
# Here, we run BOHB, but that is not essential.
# The run method will return the `Result` that contains all runs performed.
bohb = BOHB(  configspace = worker.get_configspace(),
              run_id = args.run_id,
              host=host,
              nameserver=ns_host,
              nameserver_port=ns_port,
              min_budget=args.min_budget, max_budget=args.max_budget
           )

res = bohb.run(n_iterations=args.n_iterations, min_n_workers=args.n_workers)

with open(os.path.join(args.shared_directory, 'results.pkl'), 'wb') as fh:
    pickle.dump(res, fh)

# Step 4: Shutdown
# After the optimizer run, we must shutdown the master and the nameserver.


# Step 5: Analysis
# Each optimizer returns a hpbandster.core.result.Result object.
# It holds informations about the optimization run like the incumbent (=best) configuration.
# For further details about the Result object, see its documentation.
# Here we simply print out the best config and some statistics about the performed runs.
id2config = res.get_id2config_mapping()
incumbent = res.get_incumbent_id()

# print('Best found configuration:', id2config[incumbent]['config'])
# print('A total of %i unique configurations where sampled.' % len(id2config.keys()))
# print('A total of %i runs where executed.' % len(res.get_all_runs()))
# print('Total budget corresponds to %.1f full function evaluations.'%(sum([r.budget for r in res.get_all_runs()])/args.max_budget))

def get_parameters():
    return id2config[incumbent]['config']

print(id2config[incumbent]['config'])

bohb.shutdown(shutdown_workers=True)
NS.shutdown()
