from time import sleep

def delete(handler,clients,pk):
    client = clients[pk]
    print("\nCliente seleccionado:\n",client)
        # Se puede agregar una opcion de confirmacion
    option = input("\nEsta seguro que desea eliminar este cliente y/n:")

    if option == "y":
        del clients[pk]

        for x,y in enumerate(clients):
            y["ident"] = x+1 

        handler.writer(clients)
        sleep(2)
        print("\nCliente eliminado:\n")

    else:
        print("\nEL cliente no ha sido eliminado\n")
   