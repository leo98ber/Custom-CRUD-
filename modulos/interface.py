from modulos import clients,create, handler_fields

data_base = ["id","code","name","last_name","age","email","enterprise","position","company_years"]
field_name = "Names.csv"

def interface():

    while True:
        handler = handler_fields.Handler_fields(field_name,data_base)
        info_client = create.Field_exist(field_name,data_base)
        cliente = clients.Client(handler,info_client)
        module = input('\nIndique la modalidad o presione "q" para escapar:\n')
        module = module.upper().strip()

        if module == 'C':
            cliente.create()            

        elif module == 'R':
            cliente.read()

        elif module == 'U':
            cliente.update()

        elif module == 'D':
            cliente.delete()

        elif module == 'Q':
            break

        else:
            print("\nError usted introdujo una opcion invalida intente de nuevo\n")

 
