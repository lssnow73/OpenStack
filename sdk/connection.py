from os import environ as env
from openstack import connection


DEFAULT_AUTH_URL = 'http://192.168.219.188:35357/v3'
DEFAULT_USERNAME = 'admin'
DEFAULT_PASSWORD = 'admin'
DEFAULT_PROJECT_NAME = 'admin'
DEFAULT_USER_DOMAIN_NAME = 'default'
DEFAULT_PROJECT_DOMAIN_NAME = 'default'


def create_connection(auth_url=None, username=None, password=None,
                      project_name=None, user_domain_name=None, project_domain_name=None):

    if(auth_url == None):
        try:
            auth_url = env['OS_AUTH_URL']
        except:
            auth_url = DEFAULT_AUTH_URL

    if(username == None):
        try:
            username = env['OS_USERNAME']
        except:
            username = DEFAULT_USERNAME

    if(password == None):
        try:
            password = env['OS_PASSWORD']
        except:
            password = DEFAULT_PASSWORD

    if(project_name == None):
        try:
            project_name = env['OS_PROJECT_NAME']
        except:
            project_name = DEFAULT_PROJECT_NAME

    if(user_domain_name == None):
        try:
            user_domain_name = env['OS_USER_DOMAIN_NAME']
        except:
            user_domain_name = DEFAULT_USER_DOMAIN_NAME

    if(project_domain_name == None):
        try:
            project_domain_name = env['OS_PROJECT_DOMAIN_NAME']
        except:
            project_domain_name = DEFAULT_PROJECT_DOMAIN_NAME

    try:
        conn = connection.Connection(auth_url=auth_url,
                                     username=username,
                                     password=password,
                                     project_name=project_name,
                                     user_domain_id=user_domain_name,
                                     project_domain_id=project_domain_name
                                    )
    except:
        return None

    return conn

def list_users(conn):
    print("List users:")

    for user in conn.identity.users():
        print user


if __name__ == '__main__':
    conn = create_connection()

    list_users(conn)
