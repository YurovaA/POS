import os
import sys
import fileinput
from subprocess import call
__author__ = 'anna'

filename = 'batch_mpi.cmd'
thread_number = [1]
processes_number = [1, 2, 4, 8, 16]
non_hybrid = True
for thread_num in thread_number:
    for proc_num in processes_number:
        if (thread_num*proc_num == 16 or non_hybrid):
            f = open(filename,'r')
            filedata = f.read()
            f.close()

            newdata = filedata.replace("$$NUMBER_OF_THREADS$$", str(thread_num))
            newdata = newdata.replace("$$NUMBER_OF_PROCESSES$$", str(proc_num))

            f = open(filename, 'w')
            f.write(newdata)
            f.close()

            #f = open('batch_example.cmd','r')
            filedata = newdata#f.read()
            #f.close()

            call("cat "+ filename, shell = True)

            newdata = filedata.replace("OMP_NUM_THREADS="+str(thread_num), "OMP_NUM_THREADS=$$NUMBER_OF_THREADS$$")
            newdata = newdata.replace("pos_lulesh_openmp_"+str(thread_num), "pos_lulesh_openmp_$$NUMBER_OF_THREADS$$")
            newdata = newdata.replace("mpiexec -n "+str(proc_num), "mpiexec -n $$NUMBER_OF_PROCESSES$$")
            newdata = newdata.replace("pos_lulesh_mpi_"+str(proc_num), "pos_lulesh_mpi_$$NUMBER_OF_PROCESSES$$")
            newdata = newdata.replace("pos_lulesh_hybrid_"+str(proc_num)+"_"+str(thread_num), "pos_lulesh_hybrid_$$NUMBER_OF_PROCESSES$$_$$NUMBER_OF_THREADS$$")

            f = open(filename, 'w')
            f.write(newdata)
            f.close()
