from io import BytesIO
from docker import APIClient
import docker
client = docker.from_env()
print(client.image.pull("busybox:buildroot-2014.02"))
print(client.image.list())
dockerfile = '''
#Shared folders
FROM busybox:buildroot-2014.02
VOLUME /data
CMD ["/bin/sh"]
'''
f = BytesIO(dockerfile.encode('utf-8'))
cli = APIClient(base_url='tcp://127.0.0.1:2375')
response = [line for line in cli.build(fileobj=f, rm = True, tag = 'yourname/volume')]
print(response) 
