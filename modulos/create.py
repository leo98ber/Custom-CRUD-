from modulos import token       


def in_info(client):
    ident = len(client)+1
    code = token.token()
    name = input("Introduzca su nombre: ").capitalize()
    last_name = input("Introduzca su apellido: ").capitalize()
    email = input("Introduzca su correo: ").lower()
    enterprise = input("Introduzca su empresa: ").capitalize()
    position = input("Introduzca su cargo: ")

    return  ident,code,name,last_name,email,enterprise,position
