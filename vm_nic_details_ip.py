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

# This program can be used to display Vm nic details and IP addresses assigned to them.

from ovirtsdk.api import API
from ovirtsdk.xml import params
import time


try:
    api = API(url="https://myrhevm.humblec.com/api",
              username="admin@internal",
              password="redhat",
              ca_file="/root/ca.crt")
    try:
         vmsList = api.vms.list()
         for instance in vmsList:
                print '\t \t\t\tVM :%s' % (instance.name.upper())
                address=[]
                if instance.status.state == 'up' and instance.get_guest_info():
                        vmnics= instance.get_nics().list()
                        ips = instance.get_guest_info().get_ips().get_ip()
                        for card in vmnics:
                                print 'Net.ID:%s \t Name:%s \t MacAddress:%s \t Interface:%s \t Plugged:%s \t Linked:%s ' % (card.network.id, card.name, card.mac.address, card.interface, card.plugged, card.linked)
                        for ip in ips:
                                address.append(ip.get_address())
                                print '\t IP : %s' % ( ip.get_address())
    except Exception as e:
        print 'Start VM Exception:\n%s' % str(e)


    api.disconnect()

except Exception as ex:
    print "Unexpected error: %s" % ex
