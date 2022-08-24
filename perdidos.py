#Funcion de carga y ordenamiento de lista -- usé sort() pero entregaba un none ¿?
def cargador(lista):
    pregunta = 's'
    while pregunta == 's' :
        elemento = int(input('Ingrese un valor para la cadena: '))        
        lista.append(elemento) 
        pregunta = input('Desea ingresar otro valor? (s/n) ').lower()
    lista = set(lista)
    lista_ordenada = sorted(lista)    
    return lista_ordenada


#Funcion de busqueda y generacion de listas perdidas
def perdidos(lista):
    lista_completa = []
    for i in range (0, (len(lista)-1)):          
        elementos_perdidos = [x for x in range ((lista[i])+1,lista[i+1])]
        lista_perdidos = (f'{lista [i]}  {elementos_perdidos}  {lista [i +1]}')
        lista_completa.append(lista_perdidos) 
    return lista_completa
     

lista = []
try:
    print (f'El array es {cargador(lista)} \n la lista completa junto a los elementos perdidos es {perdidos(cargador(lista))}')
except ValueError as ve:
        print ('Ingrese un valor numerico por favor')
