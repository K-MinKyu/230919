import sys

from scapy.sendrecv import sniff

import scapy

from scapy import *
#
while True:
    sniff(iface="lo0",prn=lambda x:x.show())