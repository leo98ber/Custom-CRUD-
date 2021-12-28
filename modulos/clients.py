from os import name


class Client(object):
    def __init__(self,id,name,last_name,email,enterprise,position):
        self.id = id
        self.name = name
        self.last_name = last_name
        self.email = email
        self.enterprise = enterprise
        self.position = position


    
    def create():
        pass

    
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

