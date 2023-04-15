nombres = ''' 'Agustin', 'Alan', 'Andrés', 'Ariadna', 'Bautista', 'CAROLINA', 'CESAR', 
'David','Diego', 'Dolores', 'DYLAN', 'ELIANA', 'Emanuel', 'Fabián', 'Facundo', 
'Francsica', 'FEDERICO', 'Fernanda', 'GONZALO', 'Gregorio', 'Ignacio', 'Jonathan', 
'Joaquina', 'Jorge','JOSE', 'Javier', 'Joaquín' , 'Julian', 'Julieta', 'Luciana',
'LAUTARO', 'Leonel', 'Luisa', 'Luis', 'Marcos', 'María', 'MATEO', 'Matias', 
'Nicolás', 'Nancy', 'Noelia', 'Pablo', 'Priscila', 'Sabrina', 'Tomás', 'Ulises',
'Yanina' '''
notas_1 = [81, 60, 72, 24, 15, 91, 12, 70, 29, 42, 16, 3, 35, 67, 10, 57, 11, 69,
12, 77, 13, 86, 48, 65, 51, 41, 87, 43, 10, 87, 91, 15, 44,
85, 73, 37, 42, 95, 18, 7, 74, 60, 9, 65, 93, 63, 74]
notas_2 = [30, 95, 28, 84, 84, 43, 66, 51, 4, 11, 58, 10, 13, 34, 96, 71, 86, 37,
64, 13, 8, 87, 14, 14, 49, 27, 55, 69, 77, 59, 57, 40, 96, 24, 30, 73,
95, 19, 47, 15, 31, 39, 15, 74, 33, 57, 10]
nombres = nombres.split(",")

def hacer_listado(par1,par2,par3):
    listado = {}
    i = 0
    for elem in par1:
        listado[elem] = par2[i],par3[i]
        i += 1
    return listado

def hacer_promedios(par1):
    promedios = {}
    for elem in par1:
        promediar = lambda x: (x[elem][0]+x[elem][1])/2
        promedios[elem] = promediar(par1)
    return promedios

def promedio_general(par1,par2):
    cant_alumnos = len(nombres)
    total = 0
    merge = par1 + par2
    for elem in merge:
        total += elem
    return total/cant_alumnos
def proms(par1):
    max = -1
    min = 9999
    for elem in promedios:
        if (promedios[elem]>max):
            max = promedios[elem]
            max_nom = elem
        if(promedios[elem]<min):
            min = promedios[elem]
            min_nom = elem
    return max_nom,min_nom

listado = hacer_listado(nombres,notas_1,notas_2)
promedios = hacer_promedios(listado)
print("--> El promedio general del curso es: ",promedio_general(notas_1,notas_2))
max,min = proms(promedios)
print("--> El mayor promedio es: ",max, " y el minimo es: ", min)

   