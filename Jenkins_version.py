## This is the script for checking Jenkins version 


import jenkins

server = jenkins.Jenkins('http://52.91.248.252:8080', username='Nani', password='Nani')
user = server.get_whoami()
version = server.get_version()
print('Hello %s from Jenkins %s' % (user['fullName'], version))
