
def client_doesnt_exist(func):
    def wrapper(self):
        try:
            func(self)
        except IndexError:
            print("\nEl id del cliente introducido no existe, intente de nuevo\n")
    return wrapper
    


def tag_doesnt_exist(func):
    def wrapper(self):
        try:
            func(self)
        except KeyError:
            print("\nLa etiqueta seleccionada no es valida, intente de nuevo\n")
    return wrapper
        
