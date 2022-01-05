
def client_doesnt_exist(func):
    def wrapper(self):
        try:
            func(self)
        except IndexError:
            print("El id del cliente introducido no existe, intente de nuevo")
    return wrapper
        
        
