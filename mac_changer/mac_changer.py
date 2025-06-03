#!/usr/bin/env python

import subprocess
import optparse

parser = optparse.OptionParser()
parser.add_option("-i", "--interface", dest="interface", help="Interface to change its mac address")
parser.add_option("-m", "--mac", dest="new_mac", help="New mac address")

(options, arguments) = parser.parse_args()

interface = options.interface
new_mac = options.new_mac
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