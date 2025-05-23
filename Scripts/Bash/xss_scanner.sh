#!/usr/bin/env bash
# ===========================================================================================================================================================
#  /$$      /$$           /$$                /$$$$$$                                          /$$   /$$                       /$$                 /$$      
# | $$  /$ | $$          | $$               /$$__  $$                                        |__/  | $$                      | $$                | $$      
# | $$ /$$$| $$  /$$$$$$ | $$$$$$$         | $$  \__/  /$$$$$$   /$$$$$$$ /$$   /$$  /$$$$$$  /$$ /$$$$$$   /$$   /$$        | $$        /$$$$$$ | $$$$$$$ 
# | $$/$$ $$ $$ /$$__  $$| $$__  $$ /$$$$$$|  $$$$$$  /$$__  $$ /$$_____/| $$  | $$ /$$__  $$| $$|_  $$_/  | $$  | $$ /$$$$$$| $$       |____  $$| $$__  $$
# | $$$$_  $$$$| $$$$$$$$| $$  \ $$|______/ \____  $$| $$$$$$$$| $$      | $$  | $$| $$  \__/| $$  | $$    | $$  | $$|______/| $$        /$$$$$$$| $$  \ $$
# | $$$/ \  $$$| $$_____/| $$  | $$         /$$  \ $$| $$_____/| $$      | $$  | $$| $$      | $$  | $$ /$$| $$  | $$        | $$       /$$__  $$| $$  | $$
# | $$/   \  $$|  $$$$$$$| $$$$$$$/        |  $$$$$$/|  $$$$$$$|  $$$$$$$|  $$$$$$/| $$      | $$  |  $$$$/|  $$$$$$$        | $$$$$$$$|  $$$$$$$| $$$$$$$/
# |__/     \__/ \_______/|_______/          \______/  \_______/ \_______/ \______/ |__/      |__/   \___/   \____  $$        |________/ \_______/|_______/ 
#                                                                                                           /$$  | $$                                      
#                                                                                                          |  $$$$$$/                                                                                                                                    \______/                                       
# ===========================================================================================================================================================
# ===========================================================================================================================================================
#  Script     : xss_scanner.sh
#  Auteur     : Lysius
#  Date       : 30/01/2023
#  Description: Script Bash pour lancer Xss Scanner.
# ===========================================================================================================================================================

if [ $# -lt 2 ]; then
  echo "Usage: $0 --url <url>"
  exit 1
fi
while [[ "$#" -gt 0 ]]; do
  case $1 in
    --url) TARGET="$2"; shift;;
  esac
  shift
done

echo "[*] Scanning for XSS on $TARGET"
for payload in '<script>alert(1)</script>' '" onerror=alert(1)'; do
  resp=$(curl -s -G --data-urlencode "q=$payload" "$TARGET")
  if [[ $resp == *"$payload"* ]]; then
    echo "[+] Possible XSS with payload: $payload"
  fi
done