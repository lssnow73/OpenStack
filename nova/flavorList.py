from keystone.getAuth import *
import novaclient.client as nvclient

sess = GetSession()
nova = nvclient.Client('2.1', session=sess)
flavors = nova.flavors.list()

for flavor in flavors:
    print flavor
