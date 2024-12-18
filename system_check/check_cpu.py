#!/usr/bin/env python
# coding: utf-8

# In[1]:


import platform
import multiprocessing

def get_cpu_info():
    num_cpus = multiprocessing.cpu_count()
    cpu_info = {
        'Number of CPUs': num_cpus
    }
    with open('/proc/cpuinfo', 'r') as f:
        lines = f.readlines()
        cpu_types = set()
        for line in lines:
            if line.strip() == '':
                continue
            parts = line.strip().split(':')
            if len(parts) == 2 and parts[0].strip() == 'model name':
                cpu_type = parts[1].strip()
                cpu_types.add(cpu_type)
    cpu_info['CPU Types'] = list(cpu_types)
    return cpu_info

def get_distribution_info():
    system_info = platform.uname()
    dist_info = {}
    
    with open('/etc/os-release', 'r') as f:
        lines = f.readlines()
        for line in lines:
            parts = line.strip().split('=')
            if len(parts) == 2:
                dist_info[parts[0]] = parts[1].strip('"')
    
    distribution_info = {
        'Node Name': system_info.node,
        'System': system_info.system,
        'Distribution' : dist_info['PRETTY_NAME'],
        'Release': system_info.release,
        'Version': system_info.version,
        'Machine': system_info.machine,
        'Processor': system_info.processor
    }
    return distribution_info, dist_info

distribution_info, dist_info = get_distribution_info()
print("Distribution Information:")
for key, value in distribution_info.items():
    print(f"{key}: {value}")

print('')
cpu_info = get_cpu_info()
print("CPU Information:")
for key, value in cpu_info.items():
    print(f"{key}: {value}")


# In[ ]:




