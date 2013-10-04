#! /usr/bin/python

#Author: Humble Chirammal <humble.devassy@gmail.com>

# Please make sure you are changing  below parameters in api :

#url      ="Your ovirt engine api url"
#username ="user to access the api"
#password ="password of above user"
#ca_file  ="location of ca cert file"


from ovirtsdk.api import API 
from ovirtsdk.xml import params
import time
try:
    api = API(url="https://myrhevm.humblec.com/api",
              username="admin@internal",
              password="something",
              ca_file="/root/ca.crt")
    try: 
	 vmsList = api.vms.list()
	 for i in vmsList:
		if i.status.state != 'down':
			print ' ===> Stopping %s ===>' % i.name
			i.stop()
           		while api.vms.get(name=i.name).status.state != 'down':
               			time.sleep(1)
           		else:
            			print "VM already down"
    except Exception as e:
        print 'Exception : Stop VM:\n%s' % str(e)


    api.disconnect()

except Exception as ex:
    print "Unexpected error: %s" % ex
