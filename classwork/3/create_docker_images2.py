from io import BytesIO
import docker
dockerfile = '''
# Shared Volume
FROM busybox:buildroot-2014.02
VOLUME /data
CMD ["/bin/sh"]
'''
f = BytesIO(dockerfile.encode('utf-8'))
cli = docker.from_env()
response = cli.api.build(fileobj=f, rm=True, tag='test3', decode=True)
# print(list(response))
resp=dict(response)
print(resp)
for line in resp:
    if line.keys()[1] in ('stream', 'error'):
        value = line.values()[1].strip()
        if value:
            print(value)




# for line in response:
#     if line.keys in ('stream', 'error'):
#         value = line.values()[0].strip()
#         if value:
#             print(value)