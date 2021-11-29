from Periodic_table import elements
from getpass import getpass
from getUser import  users




def userLogin(user, elements):

    registedUser = input('Ingrese usuario:')
    password_ = getpass('Ingrese password:') 
    
    key_values = user.keys()
    if registedUser not in key_values:
        print("Intente otra vez o registre un usario nuevo")
    elif user[registedUser]['password'] != password_:
        print('Las contraseñas no coinciden')
    else:
        print('Contraseña validada')

        print()
        print()
        print('###########  QUERY PERIODIC TABLE ELEMENTS  ###############')
        print()
        print()
        print(
             """ Periodic Table of Elements
              1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18
            1 H                                                  He
            2 Li Be                               B  C  N  O  F  Ne
            3 Na Mg                               Al Si P  S  Cl Ar
            4 K  Ca Sc Ti V  Cr Mn Fe Co Ni Cu Zn Ga Ge As Se Br Kr
            5 Rb Sr Y  Zr Nb Mo Tc Ru Rh Pd Ag Cd In Sn Sb Te I  Xe
            6 Cs Ba La Hf Ta W  Re Os Ir Pt Au Hg Tl Pb Bi Po At Rn
            7 Fr Ra Ac Rf Db Sg Bh Hs Mt Ds Rg Cn Nh Fl Mc Lv Ts Og

                    Ce Pr Nd Pm Sm Eu Gd Tb Dy Ho Er Tm Yb Lu
                    Th Pa U Np Pu Am Cm Bk Cf Es Fm Md No Lr"""
        )
        
        flag = True
        while flag:
            query_user_element = input("Ingrese elemento a consultar:")

            if query_user_element.isdigit() == True:
                print("La consulta no acepta valores numéricos")
            else:
                print('Simbolo químico:', elements[query_user_element]['Símbolo químico'])
                print('Nombre:', elements[query_user_element]['Nombre'])
                print('Número atómico:', elements[query_user_element]['Número atómico'])
                print('Grupo:', elements[query_user_element]['Grupo'])
                print('Peso atómico:', elements[query_user_element]['Peso atómico'])
                print('Niveles de energía:', elements[query_user_element]['Niveles de energía'])
                print()
                
                new_answer = input('¿Desea consultar algún otro elemento?(Y/N)')
                if new_answer == 'N':
                    flag = False
                    print('Saliendo del sistema...')
                elif new_answer == 'Y':
                    flag


            

usuarios = users()
elementos = elements()
userLogin(usuarios, elementos)