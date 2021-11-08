def crear_archivo (nom):
  nom=str(nom)
  archivo=nom+".txt"
  print(archivo)
  archivo_txl=open(archivo,"w")
  archivo_txl.close()
   

def adiciona_tex (archivo,text):
   
  archivo_texto = open(archivo,"a")
  archivo_texto.write(text+"\r\n")
  archivo_texto.close()


def mostrar (archivo):
  
  archivo_texto=open(archivo,"r")
  archi=archivo_texto.read()
  archivo_texto.close
  print (archi)


def extraer (archivo):
  
  lista=[]
  archivo_texto=open(archivo,"r")
  archi=archivo_texto.readlines()
  archivo_texto.close
  
  
  
  for x in range(len(archi)):
    numero=archi[x].replace("\n","")
    lista.append(numero)
    
  
  return lista
  