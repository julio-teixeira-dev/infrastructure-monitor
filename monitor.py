import socket
import time

targets = [
    "google.com",
    "github.com",
    "cloudflare.com"
]

def check_target(target):
    try:
        ip = socket.gethostbyname(target)

        start = time.time()

        connection = socket.create_connection(
            (target, 443),
            timeout=5
        )

        end = time.time()

        connection.close()

        latency = (end - start) * 1000

        print(f"- {target}")
        print(f"  IP: {ip}")
        print(f"  STATUS: ONLINE")
        print(f"  LATÊNCIA TCP: {latency:.2f} ms")

    except (socket.gaierror, socket.timeout, ConnectionRefusedError, OSError):
        print(f"- {target}")
        print("  STATUS: OFFLINE")

print("========================================")
print("       INFRASTRUCTURE MONITOR")
print("========================================")
print()

print("Targets configurados:")

for target in targets:
    check_target(target)
