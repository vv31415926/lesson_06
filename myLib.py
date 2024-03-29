import os
import shutil
import platform


def menu():
    print( '1  создать папку                               ','2  удалить (файл/папку)      ','3  копировать (файл/папку)\n',
           '4  просмотр содержимого рабочей директории     ','5  посмотреть только папки   ','6  посмотреть только файлы\n',
           '7  просмотр информации об операционной системе ','8  создатель программы       ','9  играть в викторину     \n',
           '10 мой банковский счет                         ','11 смена рабочей директории  ','12 выход                 \n'
           , sep='')
    while True:
        n = input( 'Введите номер пункта меню: ')
        if n.isdigit() == False:
            print( 'Ошибка выбора.')
        else:
            break
    return int(n)
#------------------------------------------------------
def newDir( ):
    s = input(  'Введите имя новой папки: ')
    p = os.path.join( os.getcwd(), s )
    if not os.path.exists(p):
        os.mkdir( p )
    else:
        print( 'такой файл/папка уже есть')
    return p
#------------------------------------------------------
def delDir( ):
    s = input(  'Введите имя папки для удаления: ')
    p = os.path.join( os.getcwd(), s )
    if os.path.exists( p ):
        os.rmdir( p )
    else:
        print( 'нет файла/папки: '+p )
    return p
#----------------------------------------------------
def copyFil():
    srcF = input('Введите имя файла для копирования: ')
    n = 1
    while n == 1:
        if not os.path.exists( srcF ):
            n = int(  input( 'Нет такого файла. \nОтмена: 0 \nПовтор: 1 \nввести:')   )
        else:
            n = 2
    dstF = input('Введите путь\имя файла куда копировать: ')
    n = 1
    while n == 1:
        if not os.path.exists(dstF):
            n = int(input('Нет такого пути. \nОтмена: 0 \nПовтор: 1 \nввести:'))
        else:
            n = 2
    if n == 2:
        shutil.copy( srcF, dstF )
#------------------------------------------------------
def viewDir():
    lst = os.listdir( os.getcwd() )
    print('----------------')
    print( lst )
    print('----------------')
#------------------------------------------------------
def viewOnlyDir():
    lst = os.listdir( os.getcwd() )
    print('----------------')
    lst = list(   filter(  lambda x: os.path.isdir(x), lst )    )
    print( lst )
    print('----------------')
#------------------------------------------------------
def viewOnlyFil():
    lst = os.listdir( os.getcwd() )
    print('----------------')
    lst = list(   filter(  lambda x: os.path.isfile(x), lst )    )
    print( lst )
    print('----------------')
#------------------------------------------------------
def infoOS():
    print('----------------')
    print(  platform.uname() )
    print('----------------')
#------------------------------------------------------
def infoMy():
    print('----------------')
    print(  'Создатель - Василич' )
    print('----------------')
#------------------------------------------------------
def chDir():
x    n = 1
    while n == 1:
        src = input('Введите путь на новую директорию: ')
        if not os.path.isabs(src):
            src = os.path.abspath(src)

        if not os.path.exists( src ):
            n = int(  input( 'Нет такой директории. \nОтмена: 0 \nПовтор: 1 \nввести:')   )
        else:
            if not os.path.isfile( src ):
                n = 2
            else:
                n = int(input('Вы ввели файл. \nОтмена: 0 \nПовтор: 1 \nввести:'))

    if n == 2:
        os.chdir( src )
        print( 'Текущий рабочий каталог: ', os.getcwd() )


