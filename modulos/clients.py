from modulos import delete, read,update,create,errors
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
        self.handler.creater(ident,code,name,last_name,email,enterprise,position)

    @errors.client_doesnt_exist
    def read(self):
        option = input("\nIndique que desea visualizar:\n").lower().strip()

        if option == "list_clients":
            print("\nLista de clientes\n")
            for client in self.clients:
                print("\n",client)

        elif option == "filter_clients":
            tag = input("\nIntroduzca un tag para filtrar: \n").lower().strip()
            keyword = input("\nIntroduzca informacion clave para la busqueda\n").lower().strip()
            read.search(self.clients,keyword,tag)

        elif option == "client":
            pk = int(input("\nIndique el id del cliente que desea visualizar:\n"))
            pk = pk-1
            client = self.clients[pk]
            print(client)

        elif option == "date_client":
            pk = int(input("\nIndique el id del cliente que desea visualizar:\n"))
            pk = pk-1
            client = self.clients[pk]
            ident,code,name,last_name,email,enterprise,position = client.values()
            read.option_read(ident,code,name,last_name,email,enterprise,position)

        else:
            print("\nError usted introdujo una opcion invalida intente de nuevo\n")

    @errors.client_doesnt_exist
    def update(self):
        pk = int(input("\nIndique el id del cliente que desea modificar: \n"))
        pk = pk-1
        update.option_update(self.handler,self.clients,pk)
    
    @errors.client_doesnt_exist
    def delete(self): 
        pk = int(input("\nIndique el id del cliente que desea eliminar:\n"))
        pk = pk-1
        delete.delete(self.handler,self.clients,pk)


        


