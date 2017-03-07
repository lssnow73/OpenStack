from keystone.getAuth import *
import novaclient.client as nvclient

sess = GetSession()
nova = nvclient.Client('2.1', session=sess)
servers = nova.servers.list()

for server in servers:
    print server
