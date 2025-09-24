#!/usr/bin/env bash
# install_anongt.sh
# Automates cloning and installing AnonGT on Debian-based systems (Kali)
# Usage: sudo ./install_anongt.sh
set -euo pipefail

REPO="https://github.com/gt0day/AnonGT.git"
TMPDIR="/tmp/anongt_install_$(date +%s)"
DESTDIR="/usr/share/AnonGT"
LAUNCHER="/usr/bin/anongt"
BACKUP_DIR="/root/anongt-install-backups-$(date +%s)"
DEPS=(tor iptables network-manager obfs4proxy bleachbit nyx xterm \
    firefox-esr torbrowser-launcher nscd secure-delete python3 python3-pip python3-venv git)

echo "=== AnonGT automated installer ==="
if [ "$(id -u)" -ne 0 ]; then
  echo "[!] Please run this script as root (sudo)."
  exit 2
fi

echo "[*] Creating temporary workspace: $TMPDIR"
mkdir -p "$TMPDIR"
cd "$TMPDIR"

echo "[*] Creating backup dir: $BACKUP_DIR"
mkdir -p "$BACKUP_DIR"

echo "[*] Updating package lists..."
apt update -y

echo "[*] Installing required packages (this may take a while)..."
apt install -y "${DEPS[@]}"

echo "[*] Cloning repository (shallow)..."
git clone --depth 1 "$REPO" AnonGT || {
  echo "[!] git clone failed. Check network and repo URL."
  exit 3
}

echo "[*] If an existing installation exists at $DESTDIR, backing it up..."
if [ -d "$DESTDIR" ]; then
  echo "[*] Backing up current $DESTDIR -> $BACKUP_DIR"
  mv "$DESTDIR" "$BACKUP_DIR/" || {
    echo "[!] Failed to backup existing installation. Aborting."
    exit 4
  }
fi

echo "[*] Moving new files to $DESTDIR"
mv AnonGT "$DESTDIR"

echo "[*] Creating Python venv inside $DESTDIR and installing requirements..."
cd "$DESTDIR"
python3 -m venv .venv
# Use the venv pip to install requirements; avoid using system pip
if [ -f requirements.txt ]; then
  ./.venv/bin/pip install --upgrade pip
  ./.venv/bin/pip install -r requirements.txt
else
  echo "[!] requirements.txt not found in repository. Skipping pip install."
fi

echo "[*] Creating wrapper launcher at $LAUNCHER"
cat > "$LAUNCHER" <<'EOF'
#!/bin/bash
# Wrapper to run AnonGT from venv
BASE="/usr/share/AnonGT"
if [ ! -d "$BASE/.venv" ]; then
  echo "AnonGT virtualenv not found at $BASE/.venv"
  exit 1
fi
# Run as root to allow the tool to modify network settings if it needs to
# (the user can prefix with sudo if desired)
source "$BASE/.venv/bin/activate"
python3 "$BASE/AnonGT.py"
EOF

chmod +x "$LAUNCHER"

echo "[*] Enabling and starting tor service (so AnonGT has tor available)."
systemctl enable --now tor || {
  echo "[!] Failed to enable or start tor service. Please check 'systemctl status tor'."
}

echo
echo "=== INSTALLATION COMPLETE ==="
echo "AnonGT installed to: $DESTDIR"
echo "Launcher created at: $LAUNCHER"
echo "Backup dir (if any): $BACKUP_DIR"
echo
echo "To run AnonGT:"
echo "  sudo $LAUNCHER"
echo
echo "Notes:"
echo " - The AnonGT tool itself may modify system networking (iptables/torrc) when you run it."
echo " - Review /usr/share/AnonGT and /etc/tor/torrc before running if you want to inspect changes first."
echo
echo "If you want an uninstall script, run the provided uninstall_anongt.sh (or see instructions)."

# Clean up tempdir
cd /
rm -rf "$TMPDIR"
exit 0
