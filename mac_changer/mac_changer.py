#!/usr/bin/env python

import subprocess

interface = "eth0" 
new_mac = "00:11:22:33:44:55"
print (f"[+] changing MAC address for {interface} to {new_mac}")

#don't use string concat because of command injection
#e.g. if you ask for input user could enter ls;rm -rf;
#subprocess.call(f"ifconfig {interface} down", shell=True)
#subprocess.call(f"ifconfig {interface} hw ether {new_mac}", shell=True)
#subprocess.call(f"ifconfig {interface} up", shell=True)
#subprocess.call("ifconfig", shell=True)

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])
subprocess.call(["ifconfig"])