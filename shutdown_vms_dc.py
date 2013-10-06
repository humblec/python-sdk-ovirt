#! /usr/bin/python

# Author Humble Chirammal <humble.devassy@gmail.com> | <hchiramm@redhat.com>
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


# Please make sure you are changing  below parameters in api :

#url      ="Your ovirt engine api url"
#username ="user to access the api"
#password ="password of above user"
#ca_file  ="location of ca cert file"



from ovirtsdk.api import API 
from ovirtsdk.xml import params
from threading import Thread
import time
import logging

threads=[]
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',
                    filename='/tmp/shutdown_vms.log',
                    filemode='w')
def shutdown_vms(vmObj):
	logging.info('Thread to stop %s', vmObj.name)
	try:
		vmObj.stop()
		#time.sleep(5)
	except Exception as e:
		logging.debug('Exception caught on VM stop:\n%s' % str(e))

if __name__ == "__main__":
   try:	
        api = API(url="https://myrhevm.humblec.com/api",
              username="admin@internal",
              password="somepassword",
              ca_file="/root/ca.crt")
    	try: 
		vmsList = api.vms.list()
	 	for i in vmsList:
			print i.name
			if i.status.state != 'down':
				logging.warning('%s is not down, trying to stop it' % i.name)
				threadMe = Thread(target=shutdown_vms, args=[i])
				threadMe.start()
				threads.append(threadMe)
    	except Exception as e:
        	logging.debug('Error:\n%s' % str(e))
    
    	logging.warning ('No of VMs to stop: %s' % len(threads))
    	print 'No of VMs to stop: %s' % len(threads)
    	for th in threads:
		logging.info ('Waiting  for %s to join' % th)
		th.join (30)
		if not th.isAlive():
			logging.info ('Thread : %s terminated' % (th.getName()))
		else:
			logging.debug( 'Thread : %s is still alive, you may check this task..' % (th))
    	api.disconnect()

   except Exception as ex:
   	logging.debug('Unexpected error: %s' % ex)
