# gpu_monitor.py

import GPUtil

def get_gpu_usage():
    gpus = GPUtil.getGPUs()
    if not gpus:
        return None, None

    gpu = gpus[0]
    return gpu.load * 100, gpu.temperature

if __name__ == "__main__":
    usage, temp = get_gpu_usage()
    print(f"GPU Usage: {usage}%")
    print(f"GPU Temperature: {temp}°C")
