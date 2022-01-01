from modulos import clients, handler_fields

def interface():

    while True:
        handler = handler_fields.Handler_fields()
        cliente = clients.Client(handler)
        module = input('\nIndique la modalidad o presione "q" para escapar:\n')
        module = module.upper()

        if module == 'C':
           cliente.create()            

        if module == 'R':
            option = input("\nIndique que desea visualizar:\n")
            cliente.read(option)

        if module == 'U':
            cliente.update()

        if module == 'D':
            cliente.delete()

        if module == 'Q':
            break

