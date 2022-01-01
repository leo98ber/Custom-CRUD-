
data_base = ["ident","code","name","last_name","email","enterprise","position"]
field_name = "Names.csv"

dates = {"ident":1,"code":"ninguno","name":"jose","last_name":"marquez","email":"N/A","enterprise":"N/A","position":"N/A"}

for date in dates:
    with open(field_name , 'w') as archivo: 
        writer = archivo.DictWriter(archivo, fieldnames = data_base) 
        writer.writerow(dates)
        archivo.close()


