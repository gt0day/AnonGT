from os import system
from time import sleep
from termcolor import colored
import tempfile
import subprocess
from urllib.request import urlopen
import re as r



def get_process(cmd):
    with tempfile.TemporaryFile() as tempf:
        proc = subprocess.Popen(cmd, stdout=tempf)
        proc.wait()
        tempf.seek(0)
        result = tempf.read().decode("utf-8").strip()
        return result


def start_service(s):
    cmd = ["systemctl", "is-active", s]
    service = get_process(cmd)
    if service != "active":
        system(f"sudo systemctl start {s}")
    else:
        system(f"sudo systemctl reload {s}")


# stop tor service
def stop_service(s):
    cmd = ["systemctl", "is-active", s]
    service = get_process(cmd)
    if service == "active":
        system(f"sudo systemctl stop {s}")


def getIP():
    try:
        d = str(urlopen('http://checkip.dyndns.com/').read())
        return r.compile(r'Address: (\d+\.\d+\.\d+\.\d+)').search(d).group(1)
    except:
        return "unknown"



timechange = int(input(colored("Enter every time need change (in minutes): ", "yellow"))) * 60
timereset = timechange

while 1:
    while timechange:
        mins, secs = divmod(timechange, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(colored("Timer: ", "red") ,colored(timer, "green"), end="\r")
        sleep(1)
        timechange -= 1
    stop_service("tor")
    sleep(1)
    start_service("tor")
    sleep(3)
    print(colored(f"Remote #IP: {getIP()}", "green"))
    timechange += timereset



