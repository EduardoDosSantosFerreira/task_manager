# main.py

import tkinter as tk
from cpu_monitor import get_cpu_usage, get_cpu_temperature, get_cpu_info
from gpu_monitor import get_gpu_usage
from disk_monitor import get_disk_usage
from network_monitor import get_network_usage, format_bytes
import time

class TaskManager(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Task Manager")
        self.geometry("600x600")
        
        self.cpu_usage_label = tk.Label(self, text="CPU Usage: ")
        self.cpu_usage_label.pack()
        
        self.cpu_temp_label = tk.Label(self, text="CPU Temperature: ")
        self.cpu_temp_label.pack()
        
        self.cpu_info_label = tk.Label(self, text="CPU Info: ")
        self.cpu_info_label.pack()

        self.gpu_usage_label = tk.Label(self, text="GPU Usage: ")
        self.gpu_usage_label.pack()

        self.gpu_temp_label = tk.Label(self, text="GPU Temperature: ")
        self.gpu_temp_label.pack()

        self.disk_usage_label = tk.Label(self, text="Disk Usage: ")
        self.disk_usage_label.pack()

        self.network_usage_label = tk.Label(self, text="Network Usage: ")
        self.network_usage_label.pack()

        self.update_info()

    def update_info(self):
        # CPU Info
        cpu_usage = get_cpu_usage()
        cpu_temp = get_cpu_temperature()
        cpu_info = get_cpu_info()

        self.cpu_usage_label.config(text=f"CPU Usage: {cpu_usage}%")
        self.cpu_temp_label.config(text=f"CPU Temperature: {cpu_temp}°C")
        self.cpu_info_label.config(text=f"CPU Info: {cpu_info['cores']} cores, {cpu_info['threads']} threads")

        # GPU Info
        gpu_usage, gpu_temp = get_gpu_usage()

        if gpu_usage is not None:
            self.gpu_usage_label.config(text=f"GPU Usage: {gpu_usage}%")
            self.gpu_temp_label.config(text=f"GPU Temperature: {gpu_temp}°C")
        else:
            self.gpu_usage_label.config(text="GPU Usage: N/A")
            self.gpu_temp_label.config(text="GPU Temperature: N/A")

        # Disk Info
        disks = get_disk_usage()
        disk_text = "\n".join([f"{disk['device']}: {disk['percent']}%" for disk in disks])
        self.disk_usage_label.config(text=f"Disk Usage:\n{disk_text}")

        # Network Info
        sent, recv = get_network_usage()
        time.sleep(1)
        sent_new, recv_new = get_network_usage()
        
        upload_speed = format_bytes(sent_new - sent)
        download_speed = format_bytes(recv_new - recv)

        self.network_usage_label.config(text=f"Network Usage:\nUpload: {upload_speed}/s\nDownload: {download_speed}/s")

        self.after(1000, self.update_info)

if __name__ == "__main__":
    app = TaskManager()
    app.mainloop()
