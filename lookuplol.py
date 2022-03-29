from ipwhois import IPWhois
from pprint import pprint
import sys
import country_converter as coco
import nmap
import os

hostname = sys.argv[1]
nm = nmap.PortScanner()

if len(sys.argv) != 2:
    sys.exit("usage <lookuplol.py IP>")

obj = IPWhois(sys.argv[1])
results = obj.lookup_rdap()
sourceCountry = results["asn_country_code"]
sourceISP = results["asn_description"]
sourceISP = sourceISP.removesuffix(", " + sourceCountry)
iso2_codes = coco.convert(names=sourceCountry, to='name_short')

os.system("nmap -sC -sV -Pn " + hostname)
pprint(hostname)
pprint(iso2_codes)
pprint(sourceISP)

    # Legacy scanning system
    # nm.scan(hosts=hostname, arguments='-sC -sV -Pn')
    # for host in nm.all_hosts():
    #     print('----------------------------------------------------')
    #     print('Host : %s (%s)' % (host, nm[host].hostname()))
    #     print('State : %s' % nm[host].state())
    #     for proto in nm[host].all_protocols():
    #         print('----------')
    #         print('Protocol : %s' % proto)

    #         lport = nm[host][proto].keys()
    #         sorted(lport)
    #         for port in lport:
    #             print ('port : %s\tstate : %s' % (port, nm[host][proto][port]['state']))
