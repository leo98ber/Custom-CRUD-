from modulos import clients





def interface(client):
    iden,name,l_name,ent,email,pos = client.values()
    cliente = clients.Client(iden,name,l_name,email,ent,pos)
    module = input("Indique la modalidad: ")
    module = module.upper()

    if module == 'C':
        option = input("Indtroduzca los datos de usuario: ")
        cliente.create(option)

    if module == 'R':
        option = input("Indique el item que desea visualizar: ")
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



