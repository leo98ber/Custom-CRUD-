# Para buscar datos puedo considerar volver el json un numpy array o usar comprehension
from time import sleep
def option_read(ident,code,name,last_name,email,enterprise,position):
    while True:
        item = input('\nIndique el item que desea visualizar o presione "q" para escapar:\n').lower()
             #colocar error al colcoar comando incorrecto
        if item =="id":
            print("\nId: \n",ident)
                
        elif item =="code":
            print("\nCodigo:\n ",code)

        elif item =="name":
            print("\nNombre:\n",name)

        elif item =="last_name":
            print("\nApellido:\n",last_name)

        elif item == "email":
            print("\nCorreo electronico:\n",email)

        elif item == "enterprise":
            print("\nEmpresa:\n",enterprise)

        elif item == "position":
            print("\nPosicion:\n",position)

        elif item =="q":
            break
        else: # Aqui debe ir una logica de error
            pass    

def search(list_clients,keyword,tag):# introducir metodos de texto para volver todo minuscula y eliminar espacios con los metodos de strp
    new_list = [(print("\n",client),client) for client in list_clients if client[tag] == keyword]