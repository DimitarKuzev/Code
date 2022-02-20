print("Advisor version 0.1 \n")
print ("Добре Дошли в Advisor (конзолен съветник)")
print ("""Този съветник ще ви покаже, как да инсталирате програми в Linux Ubuntu 20.04. 
          След проведен разговор, ще се опита да ви даде полезни съвети!""")

print("Как се казваш? ")
a = str(input("Напиши си името: "))
print("Здравей" + " " + a)

# define dictionary:

menu_options = {
    1: 'Option 1',
    2: 'Option 2',
    3: 'Option 3',
    4: 'Option 4',
    5: 'Exit',
}

def print_menu():
    for key in menu_options.keys():
        print (key, '--', menu_options[key] )


# other choice:
#def print_menu1():
#    print ('1 -- Option 1' )
#    print ('2 -- Option 2' )
#    print ('3 -- Option 3' )
#    print ('4 -- Option 4' )
#    print ('5 -- Exit' )

# simple if-elif-else code

option = int(input('Enter your choice: '))
if option == 1:
    print('Handle option \'Option 1\'')
elif option == 2:
    print('Handle option \'Option 2\'')
elif option == 3:
    print('Handle option \'Option 3\'')
elif option == 4:
    print('Handle option \'Option 4\'')
elif option == 5:
    print('Thanks message before exiting')
    exit()
else:
    print('Invalid option. Please enter a number between 1 and 5.')


def option1():
     print('Handle option \'Option 1\'')

def option2():
     print('Handle option \'Option 2\'')

def option3():
     print('Handle option \'Option 3\'')

def option4():
     print('Handle option \'Option 4\'')

def option5():
     print('Handle option \'Option 5\'')
     
option = int(input('Enter your choice: '))
        
#Check what choice was entered and act accordingly

if option == 1:
    option1()
elif option == 2:
    option2()
elif option == 3:
    option3()
elif option == 4:
    option4()
elif option == 5:
    print('Thanks message before exiting')
    exit()
else:
    print('Invalid option. Please enter a number between 1 and 4.')

# ...       ...        ...        ... final code

menu_options = {
    1: 'Option 1',
    2: 'Option 2',
    3: 'Option 3',
    4: 'Exit',
}

def print_menu():
    for key in menu_options.keys():
        print (key, '--', menu_options[key] )

def option1():
     print('Handle option \'Option 1\'')

def option2():
     print('Handle option \'Option 2\'')

def option3():
     print('Handle option \'Option 3\'')

if __name__=='__main__':
    while(True):
        print_menu()
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except:
            print('Wrong input. Please enter a number ...')
        #Check what choice was entered and act accordingly
        if option == 1:
           option1()
        elif option == 2:
            option2()
        elif option == 3:
            option3()
        elif option == 4:
            print('Thanks message before exiting')
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 4.')





    
