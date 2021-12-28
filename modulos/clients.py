from modulos import token

class Client(object):
    def __init__(self,id,name,last_name,email,enterprise,position):
        self.id = id
        self.name = name
        self.last_name = last_name
        self.email = email
        self.enterprise = enterprise
        self.position = position


    
    def create(self,client):
        self.id = token.token()
        self.name = input("Introduzca su nombre: ")
        self.last_name = input("Introduzca su apellido: ")
        self.email = input("Introduzca su correo: ")
        self.enterprise = input("Introduzca su empresa: ")
        self.position = input("Introduzca su cargo: ")

        

        client_1 ={ 
            'id':self.id,
            'name':self.id,
            'last_name':self.last_name,
            'email':self.email,
            'enterprise':self.enterprise,
            'position':self.position,
        },
        
        print("Clientes actual: ",client,"\n clientes nuevos: ",client_1)
        client = [client_1,client]
        print("\n ",client)
        return client
    
    def read(self,option = "client"):
        if option =="id":
            print("Id: ",self.id)

        if option =="name":
            print("Nombre: ",self.name)

        if option =="last_name":
            print("Apellido: ",self.last_name)

        if option == "email":
            print("Correo electronico: ",self.email)

        if option == "enterprise":
            print("Empresa: ",self.enterprise)

        if option == "position":
            print("Posicion: ",self.position)

        if option == "client":
            print(        
            self.id,
            self.name,
            self.last_name,
            self.email,
            self.enterprise,
            self.position,)
        
    def update():
        pass
    def delete():
        pass
    def search():
        pass

