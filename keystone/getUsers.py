from keystone.getAuth import *

sess = GetSession()
keystone = ksclient.Client(session=sess)
users = keystone.users.list()

for user in users:
    print user
