import os
import time

source= ['/home/alex/game', '/home/alex/iptv']

target_dir = '/tmp/backup'

today = target_dir + os.sep + time.strftime('%Y%m%d')

now = time.strftime('%H%M%S')

comment = input('Введите коментарий -----> ')


if len(comment) == 0:
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + \
    comment.replace(' ', '_') + '.zip'

if not os.path.exists(target_dir):
    os.mkdir(target_dir)
print('Каталог успешно создан', target_dir)

if not os.path.exists(today):
    os.mkdir(today)
print('Каталог успешно создан', today)

zip_command = "zip -qr {0} {1}".format(target, ' '.join(source))

if os.system(zip_command) == 0:
    print('резервнвя копия  успешно создана в ', target)
else:
    print('Создание резервоной копии не удалось')
