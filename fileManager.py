'''
0. В проекте ""Консольный файловый менеджер"" перейти на новую ветку для добавления нового функционала
1. В проекте создать новый модуль test_python.py
2. В модуле написать тесты для встроенных функций filter, map, sorted, а также для функций из библиотеки math:
pi, sqrt, pow, hypot. Чем больше тестов на каждую функцию - тем лучше
3. В том же проекте создать модуль test_filemanager.py для тестирования функций консольного файлового менеджера
4. В файле написать тесты для каждой "чистой" функции, чем больше тем лучше. Это могут быть функции консольного файлового
менеджера, а так же программы мой счет и программы викторина
5. (Дополнительно*) так же попробовать написать тесты для "грязных" функций, например копирования файла/папки, ...
Определение чистой функции есть в дополнительных материалах
8. Создать pull request на объединение веток master и новой ветки с тестами, прислать ссылку на pull request как решение дз
'''


from myLib import *
import victory as v
import persAccount as pa


if __name__ == '__main__':
    curDir = os.getcwd()   # текущий директорий


    goMenu=True
    while goMenu:
        nMenu = menu()

        if nMenu ==   1:
            inNewDir()
        elif nMenu == 2:
            delDir()
        elif nMenu == 3:
            copyFil()
        elif nMenu == 4:
            viewDir()
        elif nMenu == 5:
            viewOnlyDir()
        elif nMenu == 6:
            viewOnlyFil()
        elif nMenu == 7:
            infoOS()
        elif nMenu == 8:
            infoMy()
        elif nMenu == 9:
            pa.goGame()
            print('------------------')
        elif nMenu == 10:
            pa.goGame()
            print('------------------')
        elif nMenu == 11:
            chDir()
            print('------------------')
        elif nMenu == 12:
            goMenu = False
        else:
            print( 'Ошибка выбора!\n-------------')