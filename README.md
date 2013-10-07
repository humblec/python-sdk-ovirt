python-sdk-ovirt
================

Place holder for python sdk scripts which can be used for different purpose of ovirt functions.. 

ex: shutdown_vms_dc.py :

This script can be used to shutdown all the vms in a ovirt DC when required.. 

Ex:
[root@ ~]# python start_all_down_vms.py 
 
 I am logging in /tmp/start_vms_dc.log 

vm1
vm2
IPA
mailserver

No of VMs to start: 4

[root@ ~]# cat /tmp/start_vms_dc.log


2013-10-07 08:31:19,625 WARNING vm1 is not up, trying to start it
2013-10-07 08:31:19,626 INFO Thread to start vm1
2013-10-07 08:31:19,626 WARNING vm2 is not up, trying to start it
2013-10-07 08:31:19,628 WARNING IPA is not up, trying to start it
2013-10-07 08:31:19,627 INFO Thread to start vm2
2013-10-07 08:31:19,629 INFO Thread to start IPA
2013-10-07 08:31:19,629 WARNING mailserver is not up, trying to start it
2013-10-07 08:31:19,634 WARNING No of VMs to start : 4
2013-10-07 08:31:19,634 INFO Waiting  for <Thread(Thread-1, started 139808378468096)> to join
2013-10-07 08:31:19,634 INFO Thread to start mailserver
2013-10-07 08:31:19,954 DEBUG Exception caught on VM ( vm2) start:

status: 400
reason: Bad Request
detail: Cannot run VM without at least one bootable disk.
Alternatives:
-Create a disk for this VM, and rerun the VM.
-Change the boot sequence using the Edit VM command (Boot Option Sub-Tab).
-Use the Run-Once command to select a different boot option and rerun the VM.
2013-10-07 08:31:20,249 DEBUG Exception caught on VM ( IPA) start:

status: 400
reason: Bad Request
detail: Cannot run VM. There are no available running Hosts with sufficient memory in VM's Cluster .
2013-10-07 08:31:23,309 INFO Thread : Thread-1 terminated
2013-10-07 08:31:23,309 INFO Waiting  for <Thread(Thread-2, stopped 139808299022080)> to join
2013-10-07 08:31:23,309 INFO Thread : Thread-2 terminated
2013-10-07 08:31:23,309 INFO Waiting  for <Thread(Thread-3, stopped 139808288532224)> to join
2013-10-07 08:31:23,309 INFO Thread : Thread-3 terminated
2013-10-07 08:31:23,309 INFO Waiting  for <Thread(Thread-4, stopped 139808278042368)> to join
2013-10-07 08:31:23,309 INFO Thread : Thread-4 terminated
2013-10-07 08:31:23,309 DEBUG  Below Vms failed to start with an exception:['vm2', 'IPA']
You have new mail in /var/spool/mail/root
