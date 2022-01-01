from modulos import read,update,create
from time import sleep, time

class Client(object):
    def __init__(self,handler):
        self.handler = handler
        self.client = self.handler.reader()
    
    def create(self):
        print("\nIntroduzca los datos solicitados para crear el cliente\n")
        sleep(1)
        ident,code,name,last_name,email,enterprise,position = create.in_info()
        create.write(ident,code,name,last_name,email,enterprise,position)


    
    def read(self,option="list_clients"):

        if option == "list_clients":
            print("\nLista de clientes\n")
            for client in self.client:
                print("\nLista de clientes",client)

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
        pk = int(input("\nIndique el id del cliente que desea eliminar:\n"))
        pk = pk-1
        cliente = self.client[pk]
        print("\nCliente seleccionado:\n",cliente)
        # Hay que modificar el id una vez borrado el cliente, adaptando a los demas
        # Opcion, hacer un for enumerate cuyo maximo sea len+1 y asignando un nuevo indice a cada usuario con la logica de edicion del update
        # Se puede agregar una opcion de confirmacion
        del self.client[pk]
        sleep(5)
        print("\nCliente eliminado:\n")

        


