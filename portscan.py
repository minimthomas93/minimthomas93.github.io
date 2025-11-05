import sys
import socket #used to create network sockets and connect to remote hosts (the core of the port scanner).
import pyfiglet

ip = '192.168.1.6'               #target IP address to scan
open_ports =[]                   #Initializes an empty list to collect ports that are found open.
ports = range(1, 65535)          #Defines the port numbers to scan.

#Defines a function probe_port that will try to connect to a given ip:port. result=1 is a default that indicates “closed” (non-zero). The function returns 0 on success (open), 1 otherwise.

def probe_port(ip, port, result = 1): 
    try: 
        #Creates a new TCP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        sock.settimeout(0.5) 

    # Attempts to connect to (ip, port). connect_ex() returns:
	#0 on success (connection established) — which indicates the port is open.
	#A non-zero error code on failure (timed out, refused, unreachable, etc).
	#connect_ex is preferred here because it returns an error code instead of raising an exception.
        r = sock.connect_ex((ip, port))
        if r == 0: 
            result = r 
        sock.close() 
    except Exception as e: 
        pass 
    return result

for port in ports: 
    sys.stdout.flush() 
    response = probe_port(ip, port) 
    if response == 0: 
        open_ports.append(port) 
    
if open_ports: 
    print ("Open Ports are: ") 
    print (sorted(open_ports)) 
else: 
    print ("Looks like no ports are open :(")
