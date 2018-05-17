#!/usr/bin/env python
#
# Get configured interfaces using Netconf
#
# darien@sdnessentials.com
#

from ncclient import manager
import sys



# the variables below assume the user is leveraging the
# network programmability lab and accessing csr1000v
# use the IP address or hostname of your CSR1000V device
HOST = '10.1.101.11'
# use the NETCONF port for your CSR1000V device
PORT = 830
# use the user credentials for your CSR1000V device
USER = 'CISCO1'
PASS = 'CISCO'



def main():
	with manager.connect(host=HOST, port=PORT, username=USER, password=PASS, hostkey_verify=False, device_params={'name':'default'}, look_for_keys=False, allow_agent=False) as m:
		print('*** here are remote decices capabilities***')
		for capability in m.server_capabilities:
			print(capability.split('?')[0])
#     return (interfaces)

if __name__ == '__main__':
    sys.exit(main())
