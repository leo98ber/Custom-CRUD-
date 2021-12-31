from modulos import clients

def interface():
    client = []# Agregar una llave user

    while True:
        cliente = clients.Client(client)
        module = input('\nIndique la modalidad o presione "q" para escapar:\n')
        module = module.upper()

        if module == 'C':
            client = cliente.create()            

        if module == 'R':
            option = input("\nIndique que desea visualizar:\n")
            cliente.read(option)

        if module == 'U':
            cliente.update()

        if module == 'D':
            cliente.delete()

        if module == 'Q':
            break

