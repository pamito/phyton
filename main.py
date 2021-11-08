""" Reto semana 7
    Pablo Andres Mayorga
    Junio 18-2021 """


#importo el modulo de Funciones 
import funciones as fun

#pregunto la cantidad de turnos que se asignaran en el dia
cantidad=int(input("Por favor ingrese la cantidad deturnos a asignar: "))

#envia la cantidad y llama a la funcion asignar turnos
turno=fun.asignar_turno(cantidad)

fun.datos_registros(turno)# Felicitaciones hemos llegado al final de este ciclo. Hasta pronto
