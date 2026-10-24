
import os
import platform
import shutil
import psutil
from datetime import datetime

def check_server_health():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    disk = shutil.disk_usage("/")

    memory_usage = memory.percent
    disk_usage = (disk.used / disk.total) * 100

    print("=" * 40)
    print("      PYTHON SERVER HEALTH MONITOR")
    print("=" * 40)
    print(f"Time       : {datetime.now().isoformat(timespec='seconds')}")
    print(f"Hostname   : {platform.node()}")
    print(f"CPU Usage  : {cpu_usage}%")
    print(f"Memory     : {memory_usage}%")
    print(f"Disk Usage : {disk_usage:.1f}%")

    if cpu_usage > 80 or memory_usage > 80 or disk_usage > 80:
        print("Server Status: WARNING")
    else:
        print("Server Status: HEALTHY")

    print("=" * 40)

if __name__ == "__main__":
    check_server_health()
