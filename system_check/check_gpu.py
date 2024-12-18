#!/usr/bin/env python
# coding: utf-8

# # cupy

# In[1]:


import cupy as cp
import socket


# In[2]:


cp.cuda.is_available()


# In[3]:


num_gpus = cp.cuda.runtime.getDeviceCount()
hostname = socket.gethostname()
print(f'Hostname: {hostname}')
print(f'Number of available GPUs: {num_gpus}')

for i in range(num_gpus):
    print("="*30)
    gpu_info = cp.cuda.runtime.getDeviceProperties(i)
    print(f"GPU {i} Properties:")
    print("Name:", gpu_info['name'].decode())
    print("Total Memory:", gpu_info['totalGlobalMem'] / (1024**3), "GB")
    print("Multiprocessors:", gpu_info['multiProcessorCount'])
    print("CUDA Cores per Multiprocessor:", gpu_info['maxThreadsPerMultiProcessor'])
    print("Clock Rate:", gpu_info['clockRate'] / 1000, "MHz")
    print("Memory Clock Rate:", gpu_info['memoryClockRate'] / 1000, "MHz")
    print("Memory Bus Width:", gpu_info['memoryBusWidth'], "bits")
    print(f"Compute Capability: {gpu_info['major']}.{gpu_info['minor']}")


# In[4]:


cp.cuda.runtime.getDevice()


# # numba

# In[5]:


import numba
from numba import cuda


# In[6]:


cuda_available = cuda.is_available()

if cuda_available:
    gpus = numba.cuda.gpus

    print("Number of GPUs:", len(gpus))
    
    for i, gpu in enumerate(gpus):
        print("="*30)
        print(f"GPU #{i}:", gpu.name.decode())
        print(f"Compute Capability: {gpu.COMPUTE_CAPABILITY_MAJOR}.{gpu.COMPUTE_CAPABILITY_MINOR}")
        #print("Total Memory:", gpu.TOTAL_MEMORY)
        print("Max Threads Per Block:", gpu.MAX_THREADS_PER_BLOCK)
        print("Warp Size:", gpu.WARP_SIZE)
        print(f"Clock Rate: {gpu.CLOCK_RATE / 1000:g} MHz")


# In[ ]:





# In[ ]:




