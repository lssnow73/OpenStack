
from os import environ as env
import glanceclient.v2.client as glclient

glance = glclient.Client(auth_url=env['OS_AUTH_URL'],
                         username=env['OS_USERNAME'],
                         password=env['OS_PASSWORD'],
                         tenant_name=env['OS_TENANT_NAME'],
                         region_name=env['OS_REGION_NAME'])


images = glance.images.list()

print images
