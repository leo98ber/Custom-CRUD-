from modulos import clients,create, handler_fields

data_base = ["ident","code","name","last_name","email","enterprise","position"]
field_name = "Names.csv"

def interface():

    while True:
        handler = handler_fields.Handler_fields(field_name,data_base)
        info_client = create.Field_exist(field_name,data_base)
        cliente = clients.Client(handler,info_client)
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

