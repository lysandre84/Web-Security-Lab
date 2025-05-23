#!/usr/bin/env python3
"""
===========================================================================================================================================================
 /$$      /$$           /$$                /$$$$$$                                          /$$   /$$                       /$$                 /$$      
| $$  /$ | $$          | $$               /$$__  $$                                        |__/  | $$                      | $$                | $$      
| $$ /$$$| $$  /$$$$$$ | $$$$$$$         | $$  \__/  /$$$$$$   /$$$$$$$ /$$   /$$  /$$$$$$  /$$ /$$$$$$   /$$   /$$        | $$        /$$$$$$ | $$$$$$$ 
| $$/$$ $$ $$ /$$__  $$| $$__  $$ /$$$$$$|  $$$$$$  /$$__  $$ /$$_____/| $$  | $$ /$$__  $$| $$|_  $$_/  | $$  | $$ /$$$$$$| $$       |____  $$| $$__  $$
| $$$$_  $$$$| $$$$$$$$| $$  \ $$|______/ \____  $$| $$$$$$$$| $$      | $$  | $$| $$  \__/| $$  | $$    | $$  | $$|______/| $$        /$$$$$$$| $$  \ $$
| $$$/ \  $$$| $$_____/| $$  | $$         /$$  \ $$| $$_____/| $$      | $$  | $$| $$      | $$  | $$ /$$| $$  | $$        | $$       /$$__  $$| $$  | $$
| $$/   \  $$|  $$$$$$$| $$$$$$$/        |  $$$$$$/|  $$$$$$$|  $$$$$$$|  $$$$$$/| $$      | $$  |  $$$$/|  $$$$$$$        | $$$$$$$$|  $$$$$$$| $$$$$$$/
|__/     \__/ \_______/|_______/          \______/  \_______/ \_______/ \______/ |__/      |__/   \___/   \____  $$        |________/ \_______/|_______/ 
                                                                                                          /$$  | $$                                      
                                                                                                         |  $$$$$$/                                      
                                                                                                          \______/                                       
===========================================================================================================================================================
===========================================================================================================================================================
 Script     : automate_scans.py
 Auteur     : Lysius
 Date       : 30/04/2024
 Description: Script Python pour automate scans.
===========================================================================================================================================================
"""
import subprocess, sys, os
from datetime import datetime

tools = [
  ['bash','scripts/bash/nikto_scan.sh'],
  ['bash','scripts/bash/zap_scan.sh'],
  ['bash','scripts/bash/dirb_scan.sh'],
  ['bash','scripts/bash/gobuster_scan.sh'],
  ['bash','scripts/bash/nmap_scan.sh'],
  ['bash','scripts/bash/wpscan.sh'],
  ['python3','scripts/python/zap_api_scan.py'],
  ['python3','scripts/python/sqlmap_automation.py']
]

if len(sys.argv)!=2: print("Usage: automate_scans.py <target>"); sys.exit(1)
target=sys.argv[1]; ts=datetime.now().strftime("%Y%m%d_%H%M%S")
base=f"reports/all/{ts}"; os.makedirs(base, exist_ok=True)

for cmd in tools:
    print("Running",cmd[1])
    try:
        subprocess.run(cmd+[target], cwd=os.getcwd(), check=True)
    except Exception as e:
        print("Error:",e)
print("Done. Reports in", base)
