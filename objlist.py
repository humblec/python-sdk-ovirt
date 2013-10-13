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

#  This program can be used to list datacenters, hypervisors, vms in an ovirt Dc ,
#with its status..


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
APIPASS="somepassword"
CAFILE="/root/ca.crt"
LOGFILENAME="/tmp/list_setup.log"

s1= '.'
objs=["datacenters", "hosts", "vms"]

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',
                    filename=LOGFILENAME,
                    filemode='w')

def getObjInfo (obje, objlist):
	greet = s1 * 15
	print '\n %s %s %s \n'  % (greet,obje, greet)
	for obj in objlist:
		print 'Name: %30s  Status:  %30s ' % ((obj.name).upper(), (obj.status.state).upper())
		logging.info ('%13s-  Name: %30s  Status:  %30s ' % (obje, (obj.name).upper(), (obj.status.state).upper()))
	
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

			
    		except Exception as e:
        		logging.debug('Error:\n%s' % str(e))
		
    		api.disconnect()
	

	except Exception as ex:
   		logging.debug('Unexpected error: %s' % ex)
