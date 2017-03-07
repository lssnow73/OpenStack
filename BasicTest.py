from os import environ as env
from keystoneauth1.identity import v3
from keystoneauth1 import session

import keystoneclient.v3.client as ksclient
import glanceclient.v2.client as glclient
import novaclient.client as nvclient

auth = v3.Password(auth_url='http://192.168.219.188:35357/v3',
                   username='admin',
                   password='admin',
                   project_name='admin',
                   user_domain_id='default',
                   project_domain_id='default'
                   )

sess = session.Session(auth=auth)

keystone = ksclient.Client(session=sess)
projects = keystone.projects.list()
for project in projects:
    print project

glance = glclient.Client(session=sess)
images = glance.images.list()
for img in images:
    print img

nova = nvclient.Client('2.1', session=sess)
flavors = nova.flavors.list()
for flavor in flavors:
    print flavor

servers = nova.servers.list()
for server in servers:
    print server

