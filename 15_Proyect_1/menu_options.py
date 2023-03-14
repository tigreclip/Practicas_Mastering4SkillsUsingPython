def options():
    print('Program Options:')
    print('1) Add a new employee')
    print('2) List all employees')
    print('3) Delete by age range')
    print('4) Update salary given a name')
    print('5) End the program')

def menu_choice():
    option = int(input('Entre your choice (from 1 to 5)'))
    sure = ''
    if option == 1:
        pass
    elif option == 2:
        pass
    elif option == 3:
        pass
    elif option == 4:
        pass
    elif sure == 'n':
        sure = input('You choose to end the program. Are you sure? Y/N'.lower())
        option = int(input('Entre your choice (from 1 to 5)'))
    else:
        break


menu_choice()




    
