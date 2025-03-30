import threading

print("Name of Current Thread",threading.current_thread().getName()) # OLD API
print("Name of Current Thread",threading.current_thread()) # NEW API