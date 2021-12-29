def option_update(client):
    #cliente es un diccionario
    while True:
        item = input('\nIndique el item que desea modificar o presione "q" para escapar:\n').lower()
             #colocar error al colcoar comando incorrecto
                
        if item =="name":
            name = input("\nIntroduzca el nombre:\n").capitalize()
            client["name"] = name

        elif item =="last_name":
            last_name = input("\nIntroduzca el apellido:\n").capitalize()
            client["last_name"] = last_name

        elif item == "email":
            email = input("\nIntroduzca el correo:\n").lower()
            client["email"] = email

        elif item == "enterprise":
            enterprise = input("\nIntroduzca la empresa:\n").capitalize()
            client["enterprise"] = enterprise
        
        elif item == "position":
            position = input("\nIntroduzca el cargo:\n")
            client["position"] = position

        elif item =="q":
            break
        else: # Aqui debe ir una logica de error
            pass    