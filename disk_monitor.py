# disk_monitor.py

import psutil

def get_disk_usage():
    disk_usage = []
    for partition in psutil.disk_partitions():
        usage = psutil.disk_usage(partition.mountpoint)
        disk_usage.append({
            "device": partition.device,
            "mountpoint": partition.mountpoint,
            "total": usage.total,
            "used": usage.used,
            "free": usage.free,
            "percent": usage.percent
        })
    return disk_usage

if __name__ == "__main__":
    disks = get_disk_usage()
    for disk in disks:
        print(f"Device: {disk['device']}")
        print(f"Mountpoint: {disk['mountpoint']}")
        print(f"Total: {disk['total']} bytes")
        print(f"Used: {disk['used']} bytes")
        print(f"Free: {disk['free']} bytes")
        print(f"Usage: {disk['percent']}%")
        print()
