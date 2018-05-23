import boto3
import boto
import boto.utils
from boto.vpc import VPCConnection


client = boto3.client("ec2")
conn=boto.vpc.connect_to_region("us-west-2")

x_file=open('/usr/local/bin/python_scripts/groups','r')
g_lst=list()
for i in x_file:
    if i not in g_lst: g_lst.append(i)
    else:continue


##Below lines will connect to the vpc and look at the instaces (by instance IDs)##

tag_lst={}
reservations = conn.get_all_reservations()
for r in reservations:
    for inst in r.instances:


#        print inst.tags['Name']
#        print inst.groups

##Below lines will extract the Name Tag of the instance (If the Instance has a Name Tag), extract the Security Group associated with that instance and the ENI that the security group has been applied (in relation to that instance) and print out the values##

      for i in inst.tags:
          if 'Name' not in i:continue
#          print i['Name']
          for group in inst.groups:
              lst=list()
              if any(group.id not in g for g in g_lst): continue
#              else: tag_lst[inst.tags['Name']]=group.id
              print inst.tags['Name'], group.id, group.name, inst.interfaces
