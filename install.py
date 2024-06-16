from core.config.functions import check_root
from os import system, path, getlogin, chdir

system("clear")
check_root()

print("--==[ AnonGT Installer ]==--")

path1 = "/usr/share/AnonGT"
path2 = "/usr/bin/anongt"
path3 = "/var/lib/anongt"

if path.exists(path1):
    system(f"sudo rm -r {path1}")
if path.exists(path2):
    system(f"sudo rm -r {path2}")
if path.exists(path3):
    system(f"sudo rm -r {path3}")

system("sudo apt update")
system("sudo apt install -y tor iptables network-manager obfs4proxy dnsmasq resolvconf bleachbit nyx xterm onionshare-cli firefox-esr torbrowser-launcher onionshare secure-delete python3 python3-pip")
system("sudo mv ../AnonGT /usr/share/AnonGT")
system("sudo touch anongt /usr/bin")
system("sudo echo 'python3 /usr/share/AnonGT/AnonGT.py $1' > /usr/bin/anongt")
system("sudo chmod +x /usr/share/AnonGT/AnonGT.py")
system("sudo chmod +x /usr/bin/anongt")
chdir(f"/home/{getlogin()}/Desktop")
system(f"cd /home/{getlogin()}/Desktop")

system("sudo pip3 install requests bs4 scapy netifaces termcolor")
system("clear")
print("--==[ AnonGT Installed Successfully ]==--")
print("Type 'sudo anongt' to start.")
exit(0)
