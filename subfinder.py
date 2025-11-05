'''
Script for enumerate subdomain through a wordlist subdomains.txt:

	- For this we have to add all our subdomains inside a list
	- Make it as a http url
	- Send the request and check if it returns error or not.
'''

import requests     # used to send HTTP requests (like GET, POST) to web servers.
import sys          # allows access to command-line arguments and system-specific parameters.

sub_list = open("wordlists.txt").read() 
subdoms = sub_list.splitlines()         # removing the newline characters (\n), make to list of  individual lines
                                                                       
for sub in subdoms:
    sub_domains = f"http://{sub}.{sys.argv[1]}"     #sys.argv[1] gets the first command-line argument passed to the script.
    try:
        requests.get(sub_domains)                   #Sends an HTTP GET request to the URL stored in sub_domains.
    except requests.ConnectionError: 
        pass
        
else:
    print("Valid domain: ",sub_domains)   

'''
Example usage:
If subdomains.txt contains:

www
mail
blog
dev

And if you run 'python subfinder.py example.com'

We might get output like:

Valid domain: http://www.example.com (if it exists)
Valid domain: http://mail.example.com (if it exists)

'''
