
def createNewUser(users):
    for i in range(2,10):
        answer = input('¿Desea agregar un nuevo usuario? (Y/N)')

        if answer == 'Y':   
        #str_base = 'user'+ str(i)
            name = input('Ingrese nuevo nombre de usuario:')
            password = input('Ingrese nueva contraseña:')
            email = input('Ingrese email:')
            users[name] = {'id': i,'password': password, 'email': email }
        elif answer == 'N':
            break
        else:
            print('Ingrese valor válido')
            
    return users


def validateUser(complete_users):
    registedUser = input('Ingrese usuario:')
    password_ = input('Ingrese password:') 
    
    key_values = complete_users.keys()
    if registedUser not in key_values:
        print("Try again with another user or register a new one")
    elif complete_users[registedUser]['password'] != password_:
        print('Las contraseñas no coinciden')
    else:
        print('Contraseña validada')
    


def users():
    users = {
    'adminUser':{
        'id': 1, 
        'user_name': 'adminUser',
        'password': '1234567',
        'email': 'tableusuario@email.com',
        }

    }
    return users


usuarios = users()
fill_usuarios = createNewUser(usuarios)
#print(fill_usuarios['Nestor']['password']
validateUser(fill_usuarios)








    