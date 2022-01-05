from time import sleep

from modulos import errors

def option_update(handler,clients,pk):
    client = clients[pk]
    print("\nDatos del cliente seleccionado:\n",client)
    while True:
        item = input('\nIndique el item que desea modificar o presione "q" para volver al menu principal:\n').lower().strip()
                
        if item =="name":
            name = input("\nIntroduzca el nombre:\n").capitalize().strip()
            client["name"] = name
            clients[pk] = client
            handler.writer(clients)

        elif item =="last_name":
            last_name = input("\nIntroduzca el apellido:\n").capitalize().strip()
            client["last_name"] = last_name
            clients[pk] = client
            handler.writer(clients)

        elif item == "age":
            age = int(input("\nIntroduzca la edad:\n").strip())
            client["age"] = age
            clients[pk] = client
            handler.writer(clients)

        elif item == "email":
            email = input("\nIntroduzca el correo:\n").lower().strip()
            client["email"] = email
            clients[pk] = client
            handler.writer(clients)

        elif item == "enterprise":
            enterprise = input("\nIntroduzca la empresa:\n").capitalize().strip()
            client["enterprise"] = enterprise
            clients[pk] = client
            handler.writer(clients)
        
        elif item == "position":
            position = input("\nIntroduzca el cargo:\n").strip()
            client["position"] = position
            clients[pk] = client
            handler.writer(clients)

        elif item == "company_years":
            company_years = int(input("\nIntroduzca los años de servicio:\n").strip())
            client["company_years"] = company_years
            clients[pk] = client
            handler.writer(clients)

        elif item =="q":
            break

        else: 
            print("Opcion invalida")
            sleep(1.5)
            print('Introduzca una opcion valida o presione "q" para escapar')

        name,last_name,age,email,enterprise,position,company_years = client.values()     
        #errors.empty_error_func(name,last_name,age,email,enterprise,position,company_years)
