import time
import sys

def afficher_heure(heure, mode_affichage):
    heures, minutes, secondes = heure.tm_hour, heure.tm_min, heure.tm_sec
    if mode_affichage == 12:
        am_pm = "AM" if heures < 12 else "PM"
        heures = heures % 12
        heures = heures if heures != 0 else 12
        print("{:02d}:{:02d}:{:02d} {}".format(heures, minutes, secondes, am_pm))
    else:
        print("{:02d}:{:02d}:{:02d}".format(heures, minutes, secondes))

def regler_alarme():
    heures = int(input("Saisir les heures pour l'alarme (0-23): "))
    minutes = int(input("Saisir les minutes pour l'alarme (0-59): "))
    secondes = int(input("Saisir les secondes pour l'alarme (0-59): "))
    alarm_time = (heures, minutes, secondes)
    return alarm_time

def changer_mode_affichage():
    mode = int(input("Choisir le mode d'affichage (12 ou 24): "))
    if mode == 12 or mode == 24:
        return mode
    else:
        print("Entrée non valide. S'il vous plaît choisir 12 ou 24.")
        return changer_mode_affichage()

def delete_last_line():
    "Use this function to delete the last line in the STDOUT"

    #cursor up one line
    sys.stdout.write('\x1b[1A')

    #delete last line
    sys.stdout.write('\x1b[2K')
    
def mettre_en_pause():
    global pause
    pause = not pause

current_time = time.localtime() # Utilisez time.localtime() pour obtenir l'heure actuelle
alarm_time = regler_alarme()
mode_affichage = changer_mode_affichage()
pause = False
while True:
    while True:
        if not pause:
            current_time = time.localtime() # Utilisez time.localtime() pour obtenir l'heure actuelle à chaque itération de la boucle
            afficher_heure(current_time, mode_affichage)
            delete_last_line()
            if current_time.tm_hour == alarm_time[0] and current_time.tm_min == alarm_time[1] and current_time.tm_sec == alarm_time[2]:
                print("Alarme!")
            time.sleep(1)
            