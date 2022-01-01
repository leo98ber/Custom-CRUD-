from modulos import handler_fields, token,read,x       
import csv 
from os import path



class Field_exist(handler_fields.Handler_fields):
    def __init__(self,field_name,data_base):
        super().__init__(field_name,data_base) 

    def exist(self):
        exist = path.isfile(self.field_name)
        print(exist)
        if exist == True:
            ni = self.reader(self.data_base)
            ident = len(ni)+1
        else:
            ident = 1
        return ident


    def in_info(self):
        ident = self.exist()
        code = token.token()
        name = input("\nIntroduzca su nombre:\n").capitalize()
        last_name = input("\nIntroduzca su apellido:\n").capitalize()
        email = input("\nIntroduzca su correo:\n").lower()
        enterprise = input("\nIntroduzca su empresa:\n").capitalize()
        position = input("\nIntroduzca su cargo:\n")
        return  ident,code,name,last_name,email,enterprise,position
        



