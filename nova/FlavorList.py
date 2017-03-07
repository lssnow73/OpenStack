import novaclient.client as novaclient

nova = nvclient.Client('2.1', session=sess)
flavors = nova.flavors.list()
for flavor in flavors:
    print flavor

servers = nova.servers.list()
for server in servers:
    print server