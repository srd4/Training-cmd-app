import time
import vlc
import threading
from queue import Queue

ms = vlc.MediaPlayer("c:/Users/Pc/Desktop/Daniel/Música/Asap Rocky- Ms ft Lil Wayne.mp3")
#nota: Es mejor tener una sola funcion para las series, y usar correctamente las variables para que se descanse según el ejercicio.
conteo = 0

class Data_tiemptotal (threading.Thread):
    def run(self):
        global conteo
        while True:
            time.sleep(1)
            conteo += 1

def actualizar(a):
    global ex_sheet
    global conteoseries
    tiempo = "%.2f" % float(conteo/60)
    hora = time.strftime("%H:%M:%S")
    fecha = time.strftime("%d/%m/%y")
    separ = ";"
    reps = conteoreps(0)
    series = str(a-1)
    
    
    f = open(ex_sheet,"a")
    f.write(tiempo+separ+hora+separ+fecha+separ+series+separ+reps )
    f.close

c = 0
def conteoreps(n):
    global c
    c = c+n
    return str(c)


dttiempo = Data_tiemptotal()

dttiempo.start()

def serie():

    def tempo_func():
        
        global reps
        reps = int(input("¿Cuantas repeticiones hizo? "))
        global ejercicio
        conteoreps(reps)
        segundos = int(reps) * ejercicio
        minutos = segundos/60
        print("Descanso de " + "%.2f" % float(str(minutos)) + " minutos")

        for i in range(segundos):
            print("%.2f" % float(segundos/60))
            if segundos == 1:
                print("finished")
                ms.play()
                global cuenta
                cuenta += 1
            segundos = segundos - 1
            time.sleep(1)
    tempo_func()
    seguir = input("¿Siguiente serie? ")
    if seguir == "si":
        print("Haga la serie " + str(cuenta))
        ms.stop()
        serie()
    elif seguir == "no":
        print("Finalizado en " + "%.2f" % float(conteo/60) + " minutos.")
        actualizar(cuenta)
        ms.stop()
        return 0
    elif seguir == "otro":
        print("Otro ejercicio")
        print("%.2f" % float(conteo/60))
        ms.stop()
        start()

e = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
desca = [12,34,40,86,35,41,13,17,86]


def identifi(n):
    global ex_sheet
    if n == "1":
        ex_sheet = "Push ups.csv"
    elif n == "2":
        ex_sheet = "Handstand push ups.csv"
    elif n == "3":
        ex_sheet = "Hollow body position crunches.csv"
    elif n == "4":
        ex_sheet = "Front progressions.csv"
    elif n == "5":
        ex_sheet = "Pull ups.csv"
    elif n == "6":
        ex_sheet = "Pseudo-planche push ups.csv"
    elif n == "7":
        ex_sheet = "Dips.csv"
    elif n == "8":
        ex_sheet = "Lumbar holds.csv"
    elif n == "9":
        ex_sheet = "Full planche progressions.csv"
    

def start():
    global cuenta
    global que_hacer
    global e
    global desca
    global ejercicio
    que_hacer = input("\nPush ups = 1\nHandstand push ups = 2\nHollow body position crunches "
                  "= 3\nFront progressions = 4\nPull ups = 5\nPseudo-planche push ups = 6\nDips = 7\nLumbar holds = 8\nFull planche progressions = 9\n\n¿Que va a hacer? ")


    if int(que_hacer) in range(1,10):
        cuenta = int(input("¿Que serie va a hacer (número)? "))
        if int(cuenta) >= 0:
            print("Puede empezar...")
        for i in e:
            if que_hacer == i:
                identifi(i)
                ejercicio = desca[e.index(i)]
                serie()
    else:
        print("Inválido")
        start()

start()


