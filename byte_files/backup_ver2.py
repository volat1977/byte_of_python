import os
import time

source = ['/home/alex/python/ex8', '/home/alex/python/ex9']

target_dir = '/tmp/backup'

if not os.path.exists(target_dir):
    os.mkdir(target_dir)
    print('Каталог успешно создан', target_dir)

today = target_dir + os.sep + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')

if not os.path.exists(today):
    os.mkdir(today)
    print('Каталог успешно создан', today)

target = today + os.sep + now + '.zip'

zip_command = "zip -qr {0} {1}".format(target, ' '.join(source))

if os.system(zip_command) == 0:
    print('Резервная  копия успешно создана в', target)
else:
    print('Создание резервной  копии  не  удалось')