from modulos import token

class Client(object):
    def __init__(self,client):
        self.client = client
    
    def create(self):
        ident = len(self.client)+1
        code = token.token()
        name = input("Introduzca su nombre: ").capitalize()
        last_name = input("Introduzca su apellido: ").capitalize()
        email = input("Introduzca su correo: ").lower()
        enterprise = input("Introduzca su empresa: ").capitalize()
        position = input("Introduzca su cargo: ")

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

        if option == "client":
            pk = int(input("Indique el id del cliente: "))
            pk = pk-1
            cliente = self.client[pk]
            print(cliente)

        if option == "date_client":
            pk = int(input("Indique el id del cliente: "))
            pk = pk-1
            cliente = self.client[pk]
            ident,code,name,last_name,email,enterprise,position = cliente.values()

            while True:
                item = input("Indique el item que desea visualizar: ").lower()
             #colocar error al colcoar comando incorrecto
                if item =="id":
                    print("Id: ",ident)
                
                elif item =="code":
                    print("Codigo: ",code)

                elif item =="name":
                    print("Nombre: ",name)

                elif item =="last_name":
                    print("Apellido: ",last_name)

                elif item == "email":
                    print("Correo electronico: ",email)

                elif item == "enterprise":
                    print("Empresa: ",enterprise)

                elif item == "position":
                    print("Posicion: ",position)

                elif item =="c":
                    break
                else: # Aqui debe ir una logica de error
                    pass


        
    def update():
        pass
    def delete():
        pass
    def search(): # Search deberia ser un modulo de read porque se buscan datos
        pass # Para buscar datos puedo considerar volver el json un numpy array

