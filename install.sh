#!/bin/bash

if (( $EUID != 0 )); then
    echo "Please run as root"
    exit
fi

echo "AnonGT Installer"

sudo rm -r /usr/share/anongt /usr/bin/anongt /var/lib/anongt

sudo apt update
sudo apt install -y apt-transport-https lsb-release curl
echo "deb [signed-by=/usr/share/keyrings/i2p-archive-keyring.gpg] https://deb.i2p2.de/ $(dpkg --status tzdata | grep Provides | cut -f2 -d'-') main" \
  | sudo tee /etc/apt/sources.list.d/i2p.list
curl -o i2p-archive-keyring.gpg https://geti2p.net/_static/i2p-archive-keyring.gpg
gpg --keyid-format long --import --import-options show-only --with-fingerprint i2p-archive-keyring.gpg
sudo cp i2p-archive-keyring.gpg /usr/share/keyrings
sudo ln -sf /usr/share/keyrings/i2p-archive-keyring.gpg /etc/apt/trusted.gpg.d/i2p-archive-keyring.gpg
sudo rm -r i2p-archive-keyring.gpg
sudo apt update
sudo apt install -y tor iptables bleachbit nyx xterm secure-delete python3 python3-pip i2p i2p-keyring
sudo mv ../AnonGT /usr/share/AnonGT
sudo touch anongt /usr/bin
sudo echo 'python3 /usr/share/AnonGT/AnonGT.py $1' > /usr/bin/anongt
sudo chmod +x /usr/share/AnonGT/AnonGT.py
sudo chmod +x /usr/bin/anongt

sudo pip3 install netifaces termcolor

clear
echo "AnonGT Installed Successfully"
echo "Please Close The Terminal And Open New Terminal Then Type anongt."

exit;

