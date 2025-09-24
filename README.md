# AnonGT - Anonymous Ghost

###### Redirect All Traffic Through Tor Network For Kali Linux v1.0.0

___

## Description

___

> ### Script to Redirect ALL Traffic Through TOR Network Including
> ### DNS Queries For Anonymizing Entire System
> ### Killing Dangerous Applications
> ### Clear Configs & Logs
> ### Firefox Browser Anonymization
> ### Timezone Changer
> ### Mac Address Changer
> ### Change #IP Automatically
> ### Anti MITM
> ### Onion Links Search Engine
> ### Onion Links Checker
> ### Share/Receive Files Anonymously
> ### Anonymous Chat On Tor Network
> ### Host Your Website On Dark Web!
> ### Encryption/Decryption Files/Folders Using AES
> ### Encrypted Keylogger

###### Please always check for updates

## Watch Video!

___

[<img src="Screenshot.png" width="100%">](https://youtu.be/KHKwfNf-3fg "AnonGT")

## AnonGT INSTALL Step By Step

___
> 1) git clone https://github.com/gt0day/AnonGT
> 2) sudo apt update;sudo apt install -y tor iptables network-manager obfs4proxy bleachbit nyx xterm firefox-esr torbrowser-launcher nscd secure-delete python3 python3-pip python3-venv
> 3) sudo mv AnonGT /usr/share/AnonGT
> 4) sudo nano /usr/bin/anongt

#### #!/bin/bash
#### source /usr/share/AnonGT/.venv/bin/activate
#### python3 /usr/share/AnonGT/AnonGT.py

> 5) sudo chmod +x /usr/share/AnonGT/AnonGT.py;sudo chmod +x /usr/bin/anongt
> 6) cd /usr/share/AnonGT;sudo python -m venv .venv;source .venv/bin/activate
> 7) pip install --upgrade pip
> 8) pip install -r requirements.txt
> 9) Close Terminal and open new one then type "sudo anongt"


## Installer / Uninstaller scripts

This repository includes two helper scripts to simplify installing AnonGT on Debian-based systems (Kali):

- `scripts/install_anongt.sh` — clones repo, installs dependencies, creates venv, creates `/usr/bin/anongt` launcher, enables `tor`.
- `scripts/uninstall_anongt.sh` — removes launcher and moves `/usr/share/AnonGT` to a backup.

**Important warnings**
- **Run only on a VM or a machine you can snapshot/restore.** These scripts install system packages and start `tor`. The AnonGT tool itself may modify `iptables` / `torrc` when executed.
- **Do not use for illegal activity.** This project and helpers are intended for research and legitimate privacy testing only.
- **Check the LICENSE.** This repo is a fork/derivative; we preserve and include the original project license (see `LICENSE`).

**Usage**
```bash
sudo chmod +x scripts/install_anongt.sh scripts/uninstall_anongt.sh
sudo ./scripts/install_anongt.sh
# to remove:
sudo ./scripts/uninstall_anongt.sh



## Notes
___

#### Check MITM Process
> sudo ps all | grep "anti-mitm"
#### kill process
> kill PID (showing on check mitm process)

___

## Change Tor Bridge Dir
> ### https://gitlab.torproject.org/tpo/anti-censorship/team/-/wikis/Default-Bridges
> ### /etc/tor/torrc

## Change Exclude Locals
> ### /usr/share/AnonGT/core/config/config.py

## Tested On
___ 
> ### Kali Linux 2024.4

## Uninstall
___
> ### sudo rm -r /usr/share/AnonGT /usr/bin/anongt /var/lib/anongt;
