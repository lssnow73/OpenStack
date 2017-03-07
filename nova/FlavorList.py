from keystone.GetAuth import *
import novaclient.client as novaclient

sess = GetSession()
nova = novaclient.Client('2.1', session=sess)
flavors = nova.flavors.list()

for flavor in flavors:
    print flavor
