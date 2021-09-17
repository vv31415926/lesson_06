def goGame():
    persAcc = 0.0
    history=[]    # [покупка, сумма, счет]
    while True:
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')

        choice = input('Выберите пункт меню: ')
        if choice == '1':
            s = float(  input( 'Введите сумму пополнения счёта (руб):')  )
            persAcc += s
            print()

        elif choice == '2':
            t = float(   input(  'Введите сумму покупки (руб):' )   )
            if t > persAcc:
                print(  'На счету мало средств!\n')
            else:
                p = input( 'Введите, что покупаете:')
                persAcc -= t
                history.append( [p,t, persAcc] )
                print()

        elif choice == '3':
            print( 'История покупок: ')
            for v in history:
                print(  v[0] +', '+str( v[1] )+'р., Осталось на счете:'+str( v[2] ) +'р.\n' )

        elif choice == '4':
            break
        else:
            print('Неверный пункт меню')

if __name__ == '__main__':
    goGame()