#modulo de graficar
import matplotlib.pyplot as plt

#modulo de crar archivos txt
import archivo 
#clase cola
import Cola as cola
#clase fecha
from datetime import datetime
#clae grafos
import networkx as nx


def conver (lis):
  lista=[]
  lista=lis.split(",")

  return lista
  

def datos_registros (turno):
  turno=separe_turnos(turno)
  cantidad=len(turno)
  contador=1
  civil=0
  sistemas=0
  electronica=0
  me_canse=[]
  

  print("\nEl listado de turnos son: ")
  for x in turno:
	    print(f'Codigo: {x[0]} - Turno: {x[1]}\t')

     
#recorre los turnos
  while contador<=cantidad:
    
  
    alum=estu(turno[0][0])
    #valido el codigo de la carrera para que me lleve la cantidad de estudiantes inscritos
    if(alum[3]=="1"):
      civil+=1
    
    elif(alum[3]=="2"):
      sistemas+=1

    elif(alum[3]=="3"):
      electronica+=1

    else:
      print("Facultad invalida")

   
    print("Inscripcion Exitosa")
    print("Codigo: ", alum[2],"\n Fecha: ",alum[4])
    
    
    #creo una lista en el cola 
    me_canse.append(alum)
    

    #selimino el primero de la fila, llamo la funcion cola.remove(me_canse
    turno=cola.Remove(turno)
    
    print("Turno restante")
    for x in turno:
	    print(f'Codigo: {x[0]} - Turno: {x[1]}\t')
        
    contador+=1
#)
      
  print ("Alumnos Inscritos: \n")
  for alumno in me_canse:
	  print(f'Nombre: {alumno[0]} - Codigo: {alumno[1]} - fecha: {alumno[4]} \t') 

  total=civil+sistemas+electronica

  print("Total de personas inscritas: ",total ,"\n")
  print("Total de personas inscritas civil: ", civil, "\n")
  print("Total de personas inscritas Sistemas: ", sistemas, "\n")
  print("Total de personas inscritas Electronica: ", electronica, "\n")
  print("Promedio de inscritos por programa: ", total/3, "\n")

  grafos(me_canse)

  #llama a la funcion graficar y envio valores para graficar los inscritos a las facultades y el total
  graficar(total,civil,sistemas,electronica)
  
  
  
#solicitud de datos para registrar 
def estu(codigo):
  dato=[]
  nom=input("Ingrese el nombre del estudiante: ")
  edad=input("Ingrese la edad del estudiante: ")
  facu=input("Digite el codigo de la facultad:\n 1. Ingenieria de Civil\n 2. ingenieria de sistemas \n 3. Ingenieria electronica \n Codigo: ")
  codigo=codigo

  now=datetime.now().strftime('%Y-%m-%d %H:%M')
        
  dato.append(nom)
  dato.append(edad)
  dato.append(codigo)
  dato.append(facu)
  dato.append(now)

  return dato


def asignar_turno(cantidad):
  
  archi="lista_enviada_DPA.txt"
  contador=1
  inscritos=[]
  turno=[]

  archi=archivo.extraer(archi)
  print(archi)
  print("\nAsigne los turnos\n")

  while (contador<=cantidad):
    
    codigo=input("Por favor ingrese el codigo: ")
#se valida si esta la lisa del dpa
    if (codigo in archi):
      #se valida que ya no se halla registrado en un turno
      if (codigo in inscritos):
      
        print("Ya esta inscrito")
      
    
      else:
        inscritos.append(codigo)
        turno.append(codigo)
        turno.append(contador)
        
          

    else:
      print("lo sentimos no esta registrado")

    
    contador+=1
  
    
  return turno

#separa la lista de dos datos y crea una sumblita con codigo y el turno
def separe_turnos(turno):
  
  n=2
  turnos=[turno[i:i + n] for i in range(0, len(turno), n)]

  return turnos 

#Reliza un diagrama de barras y se comparan con los inscritos en cada carrera
def graficar(total,civil,sistemas,electronica):
  
  data = {'Sist.': sistemas, 'Civil': civil, 'Elec.': electronica, 'Inscr.': total}
  names = list(data.keys())
  values = list(data.values())

  fig, axs = plt.subplots(1, 3, figsize=(9, 3), sharey=True)
  axs[0].bar(names, values)
  axs[1].scatter(names, values)
  axs[2].plot(names, values)
  fig.suptitle('Diagrama Inscritos')

  plt.show()
  
#realiza grafico de grafos entre los inscritos al dpa y a la facultad 
def grafos (me_canse):
  tuplas=[]
  

  archi="lista_enviada_DPA.txt"
 #extraigo los codigos del dpa
  archi=archivo.extraer(archi)
  G = nx.Graph() # Creación de un grafo dirigido vacio

  # Adicion de nodos individuales
  G.add_node("Civil") 
  G.add_node("Sistemas") 
  G.add_node("Electronica")
  G.add_node("DPA")

  tuplas=grafo_lista(me_canse)
  listadpa=lista_dpa(archi) 
  print(listadpa)
  # Adicion de una coleccion de ejes
  G.add_edges_from(tuplas)
  G.add_edges_from(listadpa)
 
  print(archi)

  print(G.nodes()) #Imprime la lista de nodos
  #grafica los noddos y ejes enviados
  nx.draw(G, with_labels=True)

#crear listas con su codigo y a al programa que pertenece
def grafo_lista(me_canse):
  tuplas=[]
  
  for i in range(len(me_canse)):
          
    if(me_canse[i][3]=="1"):
      codigo=me_canse[i][2]
      str(codigo)
      tup=["Civil",codigo]
      
    
    elif(me_canse[i][3]=="2"):
        codigo=me_canse[i][2]
        str(codigo)
        tup=["Sistemas",codigo]
        
    
    elif(me_canse[i][3]=="3"):
        codigo=me_canse[i][2]
        str(codigo)
        tup=["Electronica",codigo]

    tuplas.append(tup)
    
  
  print(tuplas)
  
  return tuplas

#creo listas del codigo con el dpa para llevarlo al grafo y pueda implementarse
def lista_dpa(archivo):
  dpa=[]
  for x in range (len(archivo)):
    cod=archivo[x]
    list_dpa=["DPA",str(cod)]
    dpa.append(list_dpa)

  return dpa
