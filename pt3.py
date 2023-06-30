nombres=[]
infs=[]
edads=[]

def grabar():
    try:
        nombre=input('cual es nombre: ')
        nombres.append(nombre)
        inf=input('cual es su INF: ')
        infs.append(inf)
        edad=input('cual es su edad: ')
        edads.append(edad)
    except ValueError:
        print('digite un valor valido')

def imprimir():

   for x in nombres,infs,edads:
       print(x)
    
def buscar():
    try:
        buscador = input('digite el inf para buscarlo en la lista\n')
    
        if buscador in infs:
            print(f'El inf {buscador} está en la lista.')
        else:
            print(f'El inf {buscador} no está en la lista.')
    except ValueError:
        print('digite un valor valido')

def salir():
    print('muchas gracias por usar mi programa espero poder volverte a ver por aqui' )
    print('este es el adios')
    

while True:
    print('[1] GRABAR ')
    print('[2] BUSCAR')
    print('[3] IMPRIMIR')
    print('[4] SALIR')
    try:
        opc = int(input('por favor digite que opcion desea \n'))
    except ValueError:
        print('digite un valor valido')
    if opc == 1:
        grabar()
        continue
    elif opc == 2:
        buscar()
        continue
    elif opc == 3:
        imprimir()
        break
    elif opc == 4:
        salir()
        break



