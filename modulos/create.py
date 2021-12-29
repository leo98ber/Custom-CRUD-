from modulos import token       


def in_info(client):
    ident = len(client)+1
    code = token.token()
    name = input("\nIntroduzca su nombre:\n").capitalize()
    last_name = input("\nIntroduzca su apellido:\n").capitalize()
    email = input("\nIntroduzca su correo:\n").lower()
    enterprise = input("\nIntroduzca su empresa:\n").capitalize()
    position = input("\nIntroduzca su cargo:\n")

    return  ident,code,name,last_name,email,enterprise,position
