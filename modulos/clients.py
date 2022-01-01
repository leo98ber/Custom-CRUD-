from modulos import delete, read,update,create
from time import sleep, time

class Client(object):
    def __init__(self,handler,info_client):
        self.handler = handler
        self.clients = self.handler.reader()
        self.info_client = info_client
    
    def create(self):
        print("\nIntroduzca los datos solicitados para crear el cliente\n")
        sleep(1)
        ident,code,name,last_name,email,enterprise,position = self.info_client.in_info()
        self.handler.writer(ident,code,name,last_name,email,enterprise,position)


    
    def read(self,option="list_clients"):

        if option == "list_clients":
            print("\nLista de clientes\n")
            for client in self.clients:
                print("\nLista de clientes",client)

        elif option == "client":
            pk = int(input("\nIndique el id del cliente:\n"))
            pk = pk-1
            client = self.clients[pk]
            print(client)

        elif option == "date_client":
            pk = int(input("\nIndique el id del cliente:\n"))
            pk = pk-1
            client = self.clients[pk]
            ident,code,name,last_name,email,enterprise,position = client.values()
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
        pk = int(input("\nIndique el id del cliente que desea eliminar:\n"))
        pk = pk-1
        delete.delete(self.handler,self.clients,pk)


        


