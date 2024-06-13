# AnonGT - Anonymous Ghost

###### Redirect All Traffic Through Tor Network For Kali Linux v0.1.3

___

![AnonGT](anongt.png "AnonGT")

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
> ### Onion Links Generator
> ### Onion Links Checker
> ### Share/Receive Files Anonymously
> ### Anonymous Chat On Tor Network
> ### Host Your Website On Dark Web!

###### Please always check for updates

## Watch Video!

___

[<img src="https://i3.ytimg.com/vi/AWtOrG14A6s/maxresdefault.jpg" width="100%">](https://youtu.be/watch?v=AWtOrG14A6s "AnonGT")

## AnonGT Install

___
> git clone https://github.com/gt0day/AnonGT && cd AnonGT && sudo python3 install.py;

## Best Secure Start
> Changing Mac + Start + Anti MITM ;)

## Notes
___

#### Check MITM Process
> sudo ps all | grep "anti-mitm"
#### kill process
> kill PID (showing on check mitm process)

## AnonGT Commands

___

### print banner help

> ### sudo anongt

### Anonymous Mode Start

> ### sudo anongt start

### Anonymous Mode Start With Secure Tor Bridges

> ### sudo anongt start+

### Anonymous Mode Stop

> ### sudo anongt stop

### Watch Tor Traffic

> ### sudo anongt status

### Get Your #IP Address

> ### sudo anongt myip

### Change Tor Identity

> ### sudo anongt chngid

### Change #IP Automatically
> ### sudo anongt autochng

### Anti MITM
> ### sudo anongt antimitm

### Change Mac Address For All Interfaces

> ### sudo anongt chngmac

### Revert Mac Address For All Interfaces

> ### sudo anongt rvmac

### Onion Links Generator
> ### sudo anongt oniongen

### Onion Links Checker

> ### sudo anongt checko

### Anonymous Share Files
> ### sudo anongt share

### Anonymous Receive Files
> ### sudo anongt receive

### Anonymous Chat
> ### sudo anongt chat

### Host A Website
> ### sudo anongt website

### Memory Wipe & Clear Logs
> ### sudo anongt wipe

### If Shutdown Without Stop
> ### sudo anongt fix

### AnonGT Check Update

> ### sudo anongt checku

### AnonGT About

> ### sudo anongt about

## Change Tor Bridge Dir
> ### https://gitlab.torproject.org/tpo/anti-censorship/team/-/wikis/Default-Bridges
> ### /etc/tor/torrc

## Change Exclude Locals
> ### /usr/share/AnonGT/core/config/config.py

## Tested On
___ 
> ### Kali Linux 2024.2

## Uninstall
___
> ### sudo rm -r /usr/share/AnonGT /usr/bin/anongt /var/lib/anongt;
