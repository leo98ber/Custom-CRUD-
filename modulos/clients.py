from modulos import create
from modulos import read

class Client(object):
    def __init__(self,client):
        self.client = client
    
    def create(self):

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
        print("Cliente creado: ",self.client)
       

        return self.client

    
    def read(self,option="list_clients"):

        if option == "list_clients":
            print("Lista de clientes",self.client)

        elif option == "client":
            pk = int(input("Indique el id del cliente: "))
            pk = pk-1
            cliente = self.client[pk]
            print(cliente)

        elif option == "date_client":
            pk = int(input("Indique el id del cliente: "))
            pk = pk-1
            cliente = self.client[pk]
            ident,code,name,last_name,email,enterprise,position = cliente.values()
            read.option_read(ident,code,name,last_name,email,enterprise,position)

        else:
            print("Error usted introdujo una opcion invalida")# Agregar manejo de errores aqui




        
    def update():
        pass
    def delete():
        pass
    def search(): # Search deberia ser un modulo de read porque se buscan datos
        pass # Para buscar datos puedo considerar volver el json un numpy array

