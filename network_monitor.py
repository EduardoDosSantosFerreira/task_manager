# network_monitor.py

import psutil
import time

def get_network_usage():
    net_io = psutil.net_io_counters()
    return net_io.bytes_sent, net_io.bytes_recv

def format_bytes(size):
    # Convert bytes to a more readable format
    power = 1024
    n = 0
    power_labels = {0: 'B', 1: 'KB', 2: 'MB', 3: 'GB', 4: 'TB'}
    while size > power:
        size /= power
        n += 1
    return f"{size:.2f} {power_labels[n]}"

if __name__ == "__main__":
    sent, recv = get_network_usage()
    time.sleep(1)
    sent_new, recv_new = get_network_usage()

    print(f"Upload: {format_bytes(sent_new - sent)}/s")
    print(f"Download: {format_bytes(recv_new - recv)}/s")
