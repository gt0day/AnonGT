#!/usr/bin/env python3
from core.config.functions import check_root, listToString, clear, exec_command, is_started, get_user,ERROR, MSG
from core.config.librareis import sys
from core.assets.banner import banner
from core.script.Anonymous import Anonymous
from core.script.Onion import ONION
from core.script.OnionShare import OnionShare


################################################################################
#                                                                              #
# AnonGT - redirect all traffic through tor network                            #
#                                                                              #
# DESCRIPTION                                                                  #
# Script to redirect all traffic through tor network including                 #
# dns queries for anonymizing entire system                                    #
# killing dangerous applications                                               #
# clear configs & logs                                                         #
# firefox browser anonymization                                                #
# Changing Mac Address                                                         #
# Anti MITM                                                                    #
# Onion Generator Links                                                        #
# Onion Links Checker                                                          #
#                                                                              #
# AUTHORS                                                                      #
# https://t.me/gtsec                                                           #
#                                                                              #
################################################################################


def AnonGT():
    check_root()

    cmd = listToString(sys.argv[1:])
    if cmd == "start":
        Anonymous.Start()
    elif cmd == "start+":
        Anonymous.StartPlus()
    elif cmd == "stop":
        Anonymous.Stop()
    elif cmd == "status":
        Anonymous.Status()
    elif cmd == "myip":
        Anonymous.MyIP()
    elif cmd == "chngid":
        Anonymous.Change_ID()
    elif cmd == "autochng":
        # check if stopped
        if is_started() == 0:
            ERROR("Anonymous Mode is already stopped")
        else:
            exec_command(f"sudo xterm -xrm 'XTerm.vt100.allowTitleOps: false' -T 'Auto #IP Changer' -geometry 150x35 -e 'sudo python3 /usr/share/AnonGT/core/sources/auto-change.py' &")
    elif cmd == "antimitm":
        exec_command(f"sudo python3 /usr/share/AnonGT/core/sources/anti-mitm.py &")
        MSG("Anti MITM Started")
    elif cmd == "chngmac":
        Anonymous.Change_Mac()
    elif cmd == "rvmac":
        Anonymous.Reverte_Mac()
    elif cmd == "oniongen":
        ONION.onion_gen()
    elif cmd == "checko":
        ONION.check()
    elif cmd == "share":
        OnionShare.Share()
    elif cmd == "receive":
        OnionShare.Receive()
    elif cmd == "chat":
        OnionShare.Chat()
    elif cmd == "website":
        OnionShare.Website()
    elif cmd == "wipe":
        Anonymous.Wipe()
    elif cmd == "fix":
        Anonymous.Fix()
    elif cmd == "checku":
        Anonymous.CheckUpdate()
    elif cmd == "about":
        Anonymous.About()
    else:
        clear()
        banner()


if __name__ == "__main__":
    AnonGT()
