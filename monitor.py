import socket

targets = [
    "google.com",
    "github.com",
    "cloudflare.com"
]

print("========================================")
print("       INFRASTRUCTURE MONITOR")
print("========================================")
print()

print("Targets configurados:")

for target in targets:
    print(f"- {target}")

    try:
        ip = socket.gethostbyname(target)
        print(f"  IP: {ip}")
    except socket.gaierror:
        print("  STATUS: OFFLINE")
