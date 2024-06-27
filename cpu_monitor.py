# cpu_monitor.py

import psutil

def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

def get_cpu_temperature():
    # Note: This might require additional setup or might not work on all systems
    try:
        import sensors
        sensors.init()
        for chip in sensors.iter_detected_chips():
            for feature in chip:
                if 'Core' in feature.label:
                    return feature.get_value()
    except Exception as e:
        return None

def get_cpu_info():
    cpu_info = {
        "cores": psutil.cpu_count(logical=False),
        "threads": psutil.cpu_count(logical=True),
    }
    return cpu_info

if __name__ == "__main__":
    print(f"CPU Usage: {get_cpu_usage()}%")
    print(f"CPU Temperature: {get_cpu_temperature()}°C")
    print(f"CPU Info: {get_cpu_info()}")
