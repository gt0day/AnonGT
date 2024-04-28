#!/usr/bin/env python3
from core.config.functions import check_root, listToString, clear, exec_command
from core.config.librareis import sys
from core.assets.banner import banner
from core.script.Anonymous import Anonymous
from core.script.Onion import ONION


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
    elif cmd == "myinfo":
        Anonymous.MyInfo()
    elif cmd == "chngid":
        Anonymous.Change_ID()
    elif cmd == "chngmac":
        Anonymous.Change_Mac()
    elif cmd == "rvmac":
        Anonymous.Reverte_Mac()
    elif cmd == "amitm":
        exec_command("xterm -xrm 'XTerm.vt100.allowTitleOps: false' -T 'Anti MITM' -e 'python3 /usr/share/AnonGT/core/sources/anti-mitm.py' &")
        clear()
        banner()
    elif cmd == "wipe":
        Anonymous.Wipe()
    # elif cmd == "starti2p":
    #     Anonymous.StartI2P()
    # elif cmd == "stopi2p":
    #     Anonymous.StopI2P()
    elif cmd == "oniongen":
        ONION.onion_gen()
    elif cmd == "checko":
        ONION.check()
    elif cmd == "checku":
        Anonymous.CheckUpdate()
    elif cmd == "about":
        Anonymous.About()
    else:
        clear()
        banner()


if __name__ == "__main__":
    AnonGT()
