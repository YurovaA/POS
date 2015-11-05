#!/bin/bash
#@ wall_clock_limit = 00:20:00
#@ job_name = pos-lulesh-hybrid
#@ job_type = MPICH
#@ class = micro
#@ output = pos_lulesh_hybrid_$$NUMBER_OF_PROCESSES$$_$$NUMBER_OF_THREADS$$.out
#@ error = pos_lulesh_hybrid_$$NUMBER_OF_PROCESSES$$_$$NUMBER_OF_THREADS$$.out
#@ node = 1
#@ total_tasks = 16
#@ node_usage = not_shared
#@ energy_policy_tag = lulesh
#@ minimize_time_to_solution = yes
#@ island_count = 1
#@ queue
. /etc/profile
. /etc/profile.d/modules.sh
. $HOME/.bashrc
# load the correct MPI library
module unload mpi.ibm
module load mpi.intel
export OMP_NUM_THREADS=$$NUMBER_OF_THREADS$$
mpiexec -n $$NUMBER_OF_PROCESSES$$ ./lulesh2.0
