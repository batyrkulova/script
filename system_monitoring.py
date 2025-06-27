import os 
import psutil
import shutil
def cpuper():
    cpu_percent = psutil.cpu_percent(interval=1)
    cpu_count = psutil.cpu_count()
    process = psutil.Process(os.getpid())
    memory_info = process.memory_info()
    return(f"CPU Usage: {cpu_percent}. Number of CPU core is {cpu_count}, Memory usage {memory_info.rss / (1024 * 1024):.2f} MB")
print(cpuper())

import shutil

def usg():
    path = '/' 
    disk_stats = shutil.disk_usage(path)
    total_bytes = disk_stats.total
    used_bytes = disk_stats.used
    free_bytes = disk_stats.free
    total_gb = round(total_bytes / (1024**3), 2)
    used_gb = round(used_bytes / (1024**3), 2)
    free_gb = round(free_bytes / (1024**3), 2)
    return(f"Disk Usage for {path}\nTotal Space: {total_gb} GB\nUsed Space: {used_gb} GB\nFree Space: {free_gb} GB") 
print(usg())


