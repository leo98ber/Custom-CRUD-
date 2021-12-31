from modulos import token,read,x       
import csv 
from os import path

data_base = ["ident","code","name","last_name","email","enterprise","position"]

def exist():
    exist = path.isfile("Names.csv")
    print(exist)
    if exist == True:
        ni = read.read(data_base)
        ident = len(ni)+1
    else:
        ident = 1
    return ident


def in_info():
    ident = exist()
    code = token.token()
    name = input("\nIntroduzca su nombre:\n").capitalize()
    last_name = input("\nIntroduzca su apellido:\n").capitalize()
    email = input("\nIntroduzca su correo:\n").lower()
    enterprise = input("\nIntroduzca su empresa:\n").capitalize()
    position = input("\nIntroduzca su cargo:\n")
    return  ident,code,name,last_name,email,enterprise,position
    

def write(ident,code,name,last_name,email,enterprise,position):  
    temp = []
    dates = [{ 
            'ident':ident,
            'code':code,
            'name':name,
            'last_name':last_name,
            'email':email,
            'enterprise':enterprise,
            'position':position
            }]

    temp.append(dates)
    print("\nCliente creado:\n",dates)

    with open('Names.csv', 'a') as csvfile: 
        writer = csv.DictWriter(csvfile, fieldnames = data_base) 
        #writer.writeheader() # Muestra el identificador de cada columna
        writer.writerows(dates)
        csvfile.close()

    #return dates




