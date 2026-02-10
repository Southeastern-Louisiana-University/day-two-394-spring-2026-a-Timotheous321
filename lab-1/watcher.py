import os
import time

path = "logs"

print(f"Monitoring {path}...", flush=True)

while True:
    files = os.listdir(path)
    print(f"Files currently in logs: {files}", flush=True)
    time.sleep(5)
