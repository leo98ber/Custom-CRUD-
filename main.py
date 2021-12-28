from modulos import clients


client = {
            'id': '5h55pbfOPfvhdfvb55',
            'name':'Leonardo',
            'last_name':'Beroes',
            'enterprise':'Apple',
            'email':'leonardoberoes94@gmail.com',
            'position':'Juniordevelopment'
        } # Agregar una llave user


def interface_user():
    iden,name,l_name,ent,email,pos = client.values()
    module = input("Indique la modalidad: ")
    module = module.upper()

    if module == 'R':
        cliente = clients.Client(iden,name,l_name,email,ent,pos)
        option = input("Indique que desea visualizar: ")
        cliente.read(option)




def main():
    interface_user()



if __name__ == "__main__": 
    main()

