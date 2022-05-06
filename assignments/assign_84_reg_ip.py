"""
Assignment: 84
Write a Python program to retrieve the IP addresses from a log file.
Log file content: create a text file and copy below text into it and use.
ERRORM01AILFROMDEVICE1.2.3.4THISISIPADDRESS
INFOSEND02MAILTODEVICEANDROID34.23.111.66THISISDESTINATION
INFOSENDMAIL03TODEVICESTB198.111.3.1TOTHETHESOURCE
ERRORMAILTO04DEVICEANDROIDFAIL89.45.23.199RETRIVETHEDATA
"""
import re

fh = open("assign_84_logs_ip.txt", "r")
logs = fh.readlines()
ip_pat = "[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}"
for lg in logs:
    ip = re.findall(ip_pat, lg)
    if len(ip) > 0:
        print(f"IP address: {ip[0]}")
    else:
        print("IP address not found in this line.")
