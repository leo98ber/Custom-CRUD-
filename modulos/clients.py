from modulos import read,update,create
from time import sleep, time

class Client(object):
    def __init__(self,client):
        self.client = client
    
    def create(self):
        print("\nIntroduzca los datos solicitados para crear el cliente\n")
        sleep(3)
        ident,code,name,last_name,email,enterprise,position = create.in_info(self.client)

        datos = { 
            'ident':ident,
            'code':code,
            'name':name,
            'last_name':last_name,
            'email':email,
            'enterprise':enterprise,
            'position':position,
        }
        
        self.client.append(datos)
        print("\nCliente creado:\n",self.client)
       

        return self.client

    
    def read(self,option="list_clients"):

        if option == "list_clients":
            print("\nLista de clientes\n",self.client)

        elif option == "client":
            pk = int(input("\nIndique el id del cliente:\n"))
            pk = pk-1
            cliente = self.client[pk]
            print(cliente)

        elif option == "date_client":
            pk = int(input("\nIndique el id del cliente:\n"))
            pk = pk-1
            cliente = self.client[pk]
            ident,code,name,last_name,email,enterprise,position = cliente.values()
            read.option_read(ident,code,name,last_name,email,enterprise,position)

        else:
            print("\nError usted introdujo una opcion invalida\n")# Agregar manejo de errores aqui

        
    def update(self):
        pk = int(input("\nIndique el id del cliente que desea modificar: \n"))
        pk = pk-1
        cliente = self.client[pk]
        print("\nDatos del cliente seleccionado:\n",cliente)
        update.option_update(cliente)

    def delete(self):
        pass


