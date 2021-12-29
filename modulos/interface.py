from modulos import clients





def interface():
    client = []# Agregar una llave user

    while True:
        cliente = clients.Client(client)
        module = input("Indique la modalidad: ")
        module = module.upper()

        if module == 'C':
            client = cliente.create()            

        if module == 'R':
            option = input("Indique que desea visualizar: ")
            cliente.read(option)

        if module == 'U':
            option = input("Indtroduzca el item que desea modificar: ")
            cliente.update(option)

        if module == 'D':
            option = input("Indique el usuario que desea eliminar: ")
            cliente.delete(option)

        if module == 'S':
            option = input("Indique el item o usuario que desea buscar: ")
            cliente.search(option)

        if module == 'Q':
            break

