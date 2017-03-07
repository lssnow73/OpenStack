from keystone.GetAuth import *
import glanceclient.v2.client as glclient

sess = GetSession()
glance = glclient.Client(session=sess)
images = glance.images.list()

print type(images)

for img in images:
    print img
