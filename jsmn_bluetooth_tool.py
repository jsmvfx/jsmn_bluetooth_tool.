import bluetooth
import os
import sys

# Stylish "jsmn" Banner
print("""
     _     _____  __  __  _   _ 
    | |   / ____||  \/  || \ | |
    | |  | (___  | \  / ||  \| |
 _  | |   \___ \ | |\/| || . ` |
| |_| |_  ____) || |  | || |\  |
 \___/   |_____/ |_|  |_||_| \_|
""")
print("jsmn Bluetooth Pentest Tool\n")

def show_menu():
    print("\n[+] Select Attack Type:")
    print("1. Flood Attack (BlueSmack)")
    print("2. DoS Attack (Bluetooth Stack Exploit)")
    print("3. Audio Injection (Play Sound on Target)")
    print("4. Eavesdrop (Sniff Bluetooth Traffic)")
    print("5. Exit")
    choice = input("\nChoose an attack (1-5): ")
    return choice

def scan_devices():
    print("\n[+] Scanning for Bluetooth devices...")
    devices = bluetooth.discover_devices(duration=8, lookup_names=True, flush_cache=True)
    if not devices:
        print("[!] No devices found. Retry or check Bluetooth range.")
        sys.exit()
    print(f"[+] Found {len(devices)} devices:")
    for addr, name in devices:
        print(f"  - {name} ({addr})")
    return devices

def flood_attack(devices):
    print("\n[!] Starting Flood Attack (BlueSmack)...")
    for addr, name in devices:
        print(f"  Flooding {name} ({addr})...")
        # Example: os.system(f"l2ping -i hci0 -s 600 -f {addr}")

def dos_attack(devices):
    print("\n[!] Starting DoS Attack (Bluetooth Stack Exploit)...")
    for addr, name in devices:
        print(f"  Exploiting {name} ({addr})...")
        # Example: Target CVE-2020-12345 (hypothetical)

def audio_injection(devices):
    audio_file = input("\nEnter audio file path (e.g., /home/user/alert.mp3): ")
    if not os.path.exists(audio_file):
        print("[!] File not found.")
        return
    print("\n[!] Starting Audio Injection...")
    for addr, name in devices:
        print(f"  Playing audio on {name} ({addr})...")
        # Example: Use A2DP profile or obexftp

def eavesdrop(devices):
    print("\n[!] Starting Eavesdropping...")
    for addr, name in devices:
        print(f"  Sniffing traffic from {name} ({addr})...")
        # Example: os.system(f"hcidump -i hci0 -w {addr}_capture.pcap")

if __name__ == "__main__":
    try:
        while True:
            choice = show_menu()
            if choice == "5":
                print("[+] Exiting...")
                sys.exit()
            elif choice in ("1", "2", "3", "4"):
                devices = scan_devices()
                if choice == "1":
                    flood_attack(devices)
                elif choice == "2":
                    dos_attack(devices)
                elif choice == "3":
                    audio_injection(devices)
                elif choice == "4":
                    eavesdrop(devices)
            else:
                print("[!] Invalid choice. Try again.")
    except KeyboardInterrupt:
        print("\n[!] Stopped by user.")
