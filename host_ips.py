#! /usr/bin/python

# Author: Humble Chirammal <humble.devassy@gmail.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.


# Please make sure you are changing below parameters in api :



#url ="Your ovirt engine api url"
#username ="user to access the api"
#password ="password of above user"
#ca_file ="location of ca cert file"

# This program can be used to display host name, status and its IPS.

# Todo: Improve this for including more details about the host nic and its layout . v1.0.

#Configure
 
APIURL="https://myrhevm.humblec.com/api"
APIUSER="admin@internal"
APIPASS="somepassword"
CAFILE="/root/ca.crt"
#LOGFILENAME="/tmp/host_ip.log"

try:
    api = API(url=APIURL,
          username=APIUSER,
          password=APIPASS,
          ca_file=CAFILE)

    try: 
	 hostsList = api.hosts.list()
	 for instance in hostsList:
		print '\t \t\t\t Hypervisor Name :%s' % (instance.name.upper())
		address=[]
		print '\t \t\t\t Status  : %s ' % (instance.status.state)

		
		if instance.status.state:
			hostsnics= instance.nics.list()
			for ni in hostsnics:
				print ni.name
				bonded = ni.get_bonding()
				if bonded:
					#TODO- all of the slaves nic object fields are None. 
					print '\ \t\t %s \n' % (ni.name)
					slvs = bonded.get_slaves()
					slvs_nics_list = slvs.get_host_nic()
					if slvs_nics_list:
						for sl in slvs_nics_list:
							print ('Details:BootProto:%s\t get_bridged:%s \t get_mac:%s \t get_check_connectivity:%s get_sttaus:%s' % ( sl.get_boot_protocol(), sl.get_bridged(), sl.get_mac(), sl.get_check_connectivity(), sl.get_status()))
							print sl.get_name()
						print ('Number of slaves:%s' % (len(slvs_nics_list)))
				print ni.name
				ips = ni.get_ip()
				address.append(ips.get_address())
				print '\t IP : %s' % ( ips.get_address())
	
		print address
    except Exception as e:
        print 'Exception:\n%s' % str(e)


    api.disconnect()

except Exception as ex:
    print "Unexpected error: %s" % ex



