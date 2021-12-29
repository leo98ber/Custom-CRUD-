def option_read(ident,code,name,last_name,email,enterprise,position):
    while True:
        item = input("Indique el item que desea visualizar: ").lower()
             #colocar error al colcoar comando incorrecto
        if item =="id":
            print("Id: ",ident)
                
        elif item =="code":
            print("Codigo: ",code)

        elif item =="name":
            print("Nombre: ",name)

        elif item =="last_name":
            print("Apellido: ",last_name)

        elif item == "email":
            print("Correo electronico: ",email)

        elif item == "enterprise":
            print("Empresa: ",enterprise)

        elif item == "position":
            print("Posicion: ",position)

        elif item =="c":
            break
        else: # Aqui debe ir una logica de error
            pass    