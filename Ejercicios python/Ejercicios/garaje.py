sensor_salida = int(input("ESCRIBE 0 O 1 PARA SABER SI HAY O NO HAY COCHE EN LA SALIDA"))
sensor_entrada = int(input("ESCRIBE 0 O 1 PARA SABER SI HAY O NO HAY COCHE EN LA ENTRADA"))

if sensor_entrada==1:
		if sensor_salida==1 :
			semaforo_entrada=0
			semaforo_salida=0
			print("Puerta bloqueada por seguridad")
		else:
			semaforo_entrada=1
			semaforo_salida=0
			print("Puede pasar el coche de la entrada")
		
else:
		if sensor_salida==0 :
			semaforo_entrada=0
			semaforo_salida=0
			print ("En espera")
		else:
			semaforo_entrada=0
			semaforo_salida=1
			print ("Puede pasar el coche de la salida")
		
	
