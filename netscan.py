#Created and executed the file in power shell

from scapy.all import *                     #scapy to create, manipulate, update, send and receive packets

interface = "eth0"                          #which interface use to send packets
ip_range = "10.10.X.X/24"                   #ip range which we have to scan
broadcastMac = "ff:ff:ff:ff:ff:ff"          # The Ethernet broadcast MAC address. 
# When you set dst to this, the Ethernet frame is delivered to every device on the local LAN segment.

packet = Ether(dst=broadcastMac)/ARP(pdst = ip_range) #create ethernet interface, create ARP packet

ans, unans = srp(packet, timeout =2, iface=interface, inter=0.1) #receive packet reply

for send,receive in ans:                                            #ans is a tuple with send and receive packets
    print (receive.sprintf(r"%Ether.src% - %ARP.psrc%"))

'''
Commands that I used:-
apt install python3-scapy
touch arp_scan.py
nano arp_scan.py
python3 arp_scan.py

'''
