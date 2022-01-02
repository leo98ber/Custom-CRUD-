def option_update(handler,clients,pk):
    client = clients[pk]
    print("\nDatos del cliente seleccionado:\n",client)
    while True:
        item = input('\nIndique el item que desea modificar o presione "q" para escapar:\n').lower()
             #colocar error al colcoar comando incorrecto
                
        if item =="name":
            name = input("\nIntroduzca el nombre:\n").capitalize()
            client["name"] = name
            clients[pk] = client
            handler.writer(clients)

        elif item =="last_name":
            last_name = input("\nIntroduzca el apellido:\n").capitalize()
            client["last_name"] = last_name
            clients[pk] = client
            handler.writer(clients)

        elif item == "email":
            email = input("\nIntroduzca el correo:\n").lower()
            client["email"] = email
            clients[pk] = client
            handler.writer(clients)

        elif item == "enterprise":
            enterprise = input("\nIntroduzca la empresa:\n").capitalize()
            client["enterprise"] = enterprise
            clients[pk] = client
            handler.writer(clients)
        
        elif item == "position":
            position = input("\nIntroduzca el cargo:\n")
            client["position"] = position
            clients[pk] = client
            handler.writer(clients)

        elif item =="q":
            break
        else: # Aqui debe ir una logica de error
            pass    