import os
import time

#1. файлы и  каталоги  собираются  в  список
source = ['/home/alex/python/ex8', '/home/alex/python/ex9']

#2. РЕзервные  копии  должны  хранится в  основном  каталоге  резерва

target_dir = '/tmp/backup'

check_dir = "ls "+ target_dir

create_target_dir = "mkdir -p " + target_dir

if os.system(check_dir) == 0:
    print("Такой каталог уже существует")
elif os.system(check_dir) != 0:
    os.system(create_target_dir)
    print("создание папки ", target_dir)
#3. Файлы помещаются zip архив

#4. Именем Архива служит текущая дата и время
target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'

zip_command = "zip -qr {0} {1}".format(target, ' '.join(source))

if os.system(zip_command) == 0:
    print('Резервная  копия успешно создана в ', target)
else:
    print('создание резервной  копии не  удалось')
