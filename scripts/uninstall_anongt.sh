#!/usr/bin/env bash
# uninstall_anongt.sh
# Removes /usr/share/AnonGT and /usr/bin/anongt
# Usage: sudo ./uninstall_anongt.sh
set -euo pipefail

DESTDIR="/usr/share/AnonGT"
LAUNCHER="/usr/bin/anongt"

if [ "$(id -u)" -ne 0 ]; then
  echo "[!] Please run as root (sudo)."
  exit 2
fi

echo "=== Uninstall AnonGT ==="
if [ -f "$LAUNCHER" ]; then
  echo "[*] Removing launcher: $LAUNCHER"
  rm -f "$LAUNCHER"
else
  echo "[*] Launcher not found: $LAUNCHER"
fi

if [ -d "$DESTDIR" ]; then
  BACKUP="/root/AnonGT-uninstall-backup-$(date +%s)"
  echo "[*] Backing up $DESTDIR -> $BACKUP"
  mv "$DESTDIR" "$BACKUP"
  echo "[*] Removed installation directory and moved to backup."
else
  echo "[*] Installation directory not found: $DESTDIR"
fi

echo "=== Uninstall complete ==="
echo "If AnonGT modified tor or iptables configurations during runtime, those changes are NOT reverted by this script."
echo "If you need to restore original network/tor settings, use your VM snapshot or review /etc/tor/torrc and iptables rules manually."
exit 0
