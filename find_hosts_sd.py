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

# This program can be used to list datacenters, hypervisors, vms in an ovirt Dc ,
#with its status..


#  This program can be used to list datacenters, hypervisors, vms in an ovirt Dc ,
#with its status..

#Refer http://humblec.com/ovirt-find-hosts-clusters-vm-running-status-ids-storage-domain-details-ovirt-dc-pythonovirt-sdk-part-3/



# Please make sure you are changing  below parameters in api :

#url      ="Your ovirt engine api url"
#username ="user to access the api"
#password ="password of above user"
#ca_file  ="location of ca cert file"


import sys
from ovirtsdk.api import API 
from ovirtsdk.xml import params
from threading import Thread
import time
import logging

#Configure
 
APIURL="https://myrhevm.humblec.com/api"
APIUSER="admin@internal"
APIPASS="redhat"
CAFILE="/root/ca.crt"
LOGFILENAME="/tmp/list_setup.log"

s1= '.'
greet = s1 * 30
objs=["datacenters", "hosts", "vms", "clusters", "storagedomains"]
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',
                    filename=LOGFILENAME,
                    filemode='w')

def getObjInfo (obje, objlist):

	print '\n %s %s %s \n'  % (greet,obje, greet)
	
	for obj in objlist:
		
		if obje=="vms" or "hosts" or "datacenters":
			print ' %30s  :  %30s : %30s ' % ((obj.name).upper(), (obj.status.state).upper(),obj.get_id())
			logging.info ('%13s-  : %30s :  %30s  : %30s' % (obje, (obj.name).upper(), (obj.status.state).upper(), obj.get_id()))
			
			if obje =="vms" and obj.status.state != 'down':
				vmonhost = api.hosts.get(id=api.vms.get(obj.name).get_host().get_id()).get_name()
				print '\n \t\t\t \ The VM: %s is running on host %s \n' % (obj.name , vmonhost)
				logging.info( 'VM: %s is running on host %s ' % (obj.name , vmonhost))
			
			if obje =="hosts" and obj.status.state != 'down':
				hostoncluster = api.clusters.get(id=api.hosts.get(obj.name).get_cluster().get_id()).get_name()
				print '\n\t\t\t\t\t\\  %20s is part of Cluster: %s\n ' % (obj.name , hostoncluster)
				logging.info( 'host: %s is on cluster %s ' % (obj.name , hostoncluster))
				
if __name__ == "__main__":
   	try:	
        	api = API(url=APIURL,
                      username=APIUSER,
              	      password=APIPASS,
                      ca_file=CAFILE)
    		try: 
			print ' \n I am logging in %s \n' % LOGFILENAME

			for ob in objs:
				if ob=="datacenters":
					getObjInfo(ob, api.datacenters.list())
				
				if ob=="hosts":
					getObjInfo(ob, api.hosts.list())
				
				if ob=="vms":
					getObjInfo(ob, api.vms.list())

				if ob=="clusters":
					print '\n %s %s %s \n'  % (greet,ob, greet)
					
					for cluster in api.clusters.list():
						print '%s \t %s' % ( cluster.name, cluster.get_id())
						logging.info( '%s \t %s' % ( cluster.name, cluster.get_id()))
				
				if ob=="storagedomains":
					print '\n %s %s %s \n'  % (greet,ob, greet)
					print '\t\tName \t\t ID \t\t\t MASTER \t\t\t\tSD.FORMAT \t\t SD.TYPE'
					
					for sd in api.storagedomains.list():
						print '%20s %20s :%20s %20s %20s' % (sd.name, sd.get_id(), sd.get_master(), sd.get_storage_format(), sd.get_type() )
						logging.info('%20s %20s :%20s %20s %20s' % (sd.name, sd.get_id(), sd.get_master(), sd.get_storage_format(), sd.get_type() ))
    		
    		except Exception as e:
        		logging.debug('Error:\n%s' % str(e))
		
    		api.disconnect()
	

	except Exception as ex:
   		logging.debug('Unexpected error: %s' % ex)
