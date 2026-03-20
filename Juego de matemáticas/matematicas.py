Nombre=input("Hola como te llamas")
Contraseña = int(input("Crea tu contraseña (Solo números)"))
Archivo=open("Contraseña.txt","a")
Archivo.write("Jugador"+Nombre+"\n")
Archivo.write(f"Jugador:"+str(Contraseña)+"\n")
Archivo.close()
print("Mucho gusto" ,Nombre, "bienvevido al quiz de matematicas, espero que hayas estudiando para responder.")
print("Ese quiz es de sexto, sino eres de sexto entonces no te vayas podrias repasar.")
print("Bueno",Nombre,"te voy a preguntar multiplicaciones, divisiones, sumas y restas.")
print("¿Calculadora? no hay problema aunque te recomiendo no usarla para aprender más")
print("Todo es gratis en ese juego")
Respuestas_si= ["Si", "si", "Ok", "ok", "Claro", "claro", "Dale", "dale"]
Respuestas_no=["No", "no", "Para nada", "para nada"]
Respuestas_si_2=["Si", "si", "Ok", "ok", "Claro", "claro", "Dale", "dale"]
Respuestas_no_2=["No", "no", "Para nada", "para nada"]
Respuestas_si_3=["Si", "si", "Ok", "ok", "Claro", "claro", "Dale", "dale"]
Respuestas_no_3=["No", "no", "Para nada", "para nada"]
Respuestas_si_4=["Si", "si", "Ok", "ok", "Claro", "claro", "Dale", "dale"]
Respuestas_no_4=["No", "no", "Para nada", "para nada"]
Respuestas_si_1_guardar_el_juego=["Si", "si", "Ok", "ok", "Claro", "claro", "Dale", "dale"]
Respuestas_no_1_guardar_el_juego=["No", "no", "Para nada", "para nada"]
Respuestas_si_2_guardar_el_juego=["Si", "si", "Ok", "ok", "Claro", "claro", "Dale", "dale"]
Respuestas_no_2_guardar_el_juego=["No", "no", "Para nada", "para nada"]
while True:
    Inicia_el_juego=input(f"¿Estas listo {Nombre}?")
    if Inicia_el_juego in Respuestas_si:
        print("Bueno, iniciemos")
        break
    elif Inicia_el_juego in Respuestas_no:
        print("Bueno, hasta la proxima,",Nombre)
        exit()
    else:
        print("Disculpa no te entendí")
print("Tómate tu tiempo para responder")
Racha=0
puntaje=0
Pregunta_1=input("Cuanto es 50+90")
if Pregunta_1== "140":
    print("Correcto")
    puntaje +=1
    Racha +=1
else:
    print("Incorrecto es 140")
    Racha=0
Pregunta_2=input("Cuánto es 200+400")
if Pregunta_2== "600":
    print("Correcto")
    puntaje +=1
    Racha +=1
else:
    print("Incorrecto es 600")
    Racha=0
Pregunta_3=input("Cuánto es 8X10")
if Pregunta_3== "80":
    print("Correcto")
    puntaje +=1
    Racha +=1
else:
    print("Incorrecto es 80")
    Racha=0
Pregunta_4=input("Cuánto es 8X9")
if Pregunta_4=="72":
    print("Correcto")
    puntaje +=1
    Racha +=1
else:
    print("Incorrecto es 72")
    Racha=0
while True:
    preparate_para_las_divisiones=input(f"Ok antes de responder la pregunta 5 {Nombre} Necesito que sepas que dividir es el signo (/) no el clasico, ok?")
    if preparate_para_las_divisiones in Respuestas_si_2:
        print("Ok,",Nombre, "Esa es la actitud")
        break
    elif preparate_para_las_divisiones in Respuestas_no_2:
        Seguro= input("¿Oye estas seguro? por favor no te rindas puedes entender eso mira 8/2=4 es lo mismo solo es que es / por favor sigue asi")
        if Seguro in Respuestas_si_3:
            print("Ok,",Nombre, "Esa es la actitud")
            break
        elif Seguro in Respuestas_no_3:
            print("Perdiste")
            print(f"Tu puntaje fue {puntaje}")
            print(f"Tu racha fue {Racha}")
        Archivo= open("resultados txt", "a")
        Quejas=input("Te gusto el juego, escribe tu opinion")
        Archivo.write("Jugador:"+Nombre+"\n")
        Archivo.write("Opinion:"+Quejas+"\n" )
        print("Gracias por su opinión")
        Archivo.close()
        exit()
    else:
        print("Disculpa no te entendí")
import time
print("Ok, tienes 5 segundos para prepararte")
time.sleep(5)
print("Empiezaaaaaaa")
print("Tómate tu tiempo para responder")
Pregunta_5=input("Cuánto es 40/8") 
if Pregunta_5=="5":
    print("Correcto")
    puntaje +=1
    Racha +=1
else:
    print("Incorrecto es 5")
    Racha=0
Pregunta_6=input("Cuánto es 20/2")
if Pregunta_6=="10":
    print("Correcto")
    puntaje +=1
    Racha +=1
else:
    print("Incorrecto es 10")
    Racha=0
Pregunta_7=input("Cuánto es 100-200")
if Pregunta_7=="-100":
    print("Correcto")
    puntaje +=1
    Racha +=1
else:
    print("Incorrecto es -100")
    Racha=0
Pregunta_8=input("Cuánto es 2000-500")
if Pregunta_8=="1500":
    print("Correcto")
    puntaje +=1
    Racha +=1
else:
    print("Incorrecto es 1500")
    Racha=0
print("¡Bien hecho! si no has respondido ninguna no hay problema hay dos preguntas dificiles")
while True:
    Bonus_time=input("¿Quieres esas preguntas no son obligatorias solo son para mejorar el puntuaje?")
    if Bonus_time in Respuestas_si_4:
        import time
        print("Ok preparate en 10 segundos porque esas preguntas si van a ser díficiles y con temporizador")
        time.sleep(10)
        Inicio=time.time()
        Pregunta_9=input("Cuánto es 12X12")
        Fin=time.time()
        if Fin - Inicio>5:
            print("Hey se acabo el tiempo es 144")
            Racha=0
        elif Pregunta_9=="144":
            print("¡Correcto!")
            puntaje +=2
            Racha +=1
        else:
            print("Incorrecto es 144")
            Racha=0
        import time
        print("Vaya respondiste la 9 pero sera difícil la 10")
        time.sleep(5)
        print("¡Preparado!")
        time.sleep(5)
        print("¡listo!")
        time.sleep(5)
        print("¡Fuera!")
        time.sleep(1)
        Inicio=time.time()
        Pregunta_10=input("Cuanto es 10X10")
        Fin=time.time()
        if Fin - Inicio>5:
            print("Hey se acabo el tiempo es 100")
            Racha=0
            break
        elif Pregunta_10=="100":
            print("¡Correcto!")
            puntaje +=2
            Racha +=1
            break
        else:
            print("Incorrecto es 100")
            Racha=0
            break
    elif Bonus_time in Respuestas_no_4:
     print("Ok")
     time.sleep(5)
     break
    else:
     print("No entendí")
while True:
         Ya_inicia=["Ya", "ya", "Vamos", "vamos","Con toda", "con toda", "Inicia","inicia"]
         Ya_termina=["No más", "no más", "No más por favor", "no más por favor", "Ya estoy cansado", "ya estoy cansado", "No quiero más", "no quiero más", "Me voy", "me voy", "Chao", "chao", "Adios", "Adios"]
         Pausa=input("Puedes descansar me avisas cuando quieres continuar (Cancelar eso escribiendo, colocando entre o puedes rechazar y eso deja el juego )")
         if Pausa in Ya_inicia:
            print("Listo ya termino el tiempo espero que hagas descansado")
            Quejas_1=input("¿Todo esta bien en el juego jugador? (Te vamos a preguntar muchas veces a continuación del juego) Sino tienes nada colocar NA, tambien aceptamos quejas de ortografía")
            Archivo=open("Quejas.txt", "a")
            Archivo.write("Jugador:"+Nombre+"\n")
            Archivo.write("Jugador:"+Quejas_1+"\n")
            Archivo.close()
            break
print("Tu puntaje:",puntaje,)
print("Tu racha:",Racha,)
if puntaje >= 10:
    print("Vaya tienes un buen puntaje")
elif puntaje < 10 and puntaje >= 5:
    print("Buen puntaje aunque puedes hacerlo mejor")
else:
    print("Puedes hacerlo mejor")
if Racha >=10:
    print("Vaya tienes una buena racha")
elif Racha <10 and Racha >=5:
     print("Buen racha aunque puedes hacerlo mejor")
else:
    print("Puedes hacerlo mejor")
Tabla_si=["Si", "si", "Ok", "ok", "Claro", "claro", "Dale", "dale"]
Tabla_no=["No", "no", "Para nada", "para nada"]
while True:
 Tabla=input("¿Quieres estar en la tabla de clasificación?")
 if Tabla in Tabla_si:
    Archivo=open("Esas personas quieren estar en la tabla","a")
    Archivo.write(f"Jugador {Nombre} quiere estar en la tabla\n")
    Archivo.close()
    break
 elif Tabla in Tabla_no:
    print("Esta bien")
    break
 else:
    print("Disculpa no entendí")
while True:
 import time
 Reiniciar=input("Quieres reiniciar el progreso")
 if Reiniciar in Respuestas_si_2_guardar_el_juego:
    print("Vas a salir en 10 segundos")
    time.sleep(10)
    exit()
 elif Reiniciar in Respuestas_no_2_guardar_el_juego:
   print("Ok, por lo que no vas a reiniciar el juego")
   break
 else:
     print("No entendí")
while True:
    Guardar_el_juego=input("Quieres guardar el juego")
    if Guardar_el_juego in Respuestas_si_1_guardar_el_juego:
        print("El juego se va a guardar")
        Archivo=open("Guardar.txt","a")
        Archivo.write(f"El jugador que quiere guardar es:{Nombre} \n")
        Archivo.write(f"El jugador que quiere guardar tiene:{puntaje} \n")
        Archivo.write(f"El jugador que quiere guardar tiene:{Racha} \n")
        Archivo.close()
        exit()
    elif Guardar_el_juego in Respuestas_no_1_guardar_el_juego:
        print("Ok no se va a guardar el juego")
        break
    else:
        print("No entendí")