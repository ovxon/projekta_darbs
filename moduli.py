import time
import random

def limena_izvele(): #pieprasa lietotājam grūtības līmeni
    global grutibas_limenis, x, y
    while True:
        grutibas_limenis = input("Izvēlieties grūtības līmeni no 1-3 (1 ir visvieglākais, 3 - visgrūtākais): ")
        time.sleep(0.5)
        try:
            grutibas_limenis = int(grutibas_limenis)
            if grutibas_limenis in range(1, 4):
                break
            elif grutibas_limenis > 3: 
                print("Ievadīta pārāk liela vērtība, mēģiniet vēlreiz")
            elif grutibas_limenis < 1:
                print("Ievadīta pārāk maza vērtība, mēģiniet vēlreiz")
                time.sleep(0.5)
        except ValueError:
            print("Ievadītā vērtība nav skaitlis, mēģiniet vēlreiz")
            time.sleep(0.5)
    x, y = grutibas_limenis + 2, grutibas_limenis + 2

def laukuma_izveide(): #izveido laukumu
    global laukums, redzamais_laukums, laukuma_kopija
    laukums = [["o" for i in range(x)] for j in range(y)]
    laukums = tuple(laukums)
    redzamais_laukums = [["o" for i in range(x)] for j in range(y)]
    laukuma_kopija = tuple(laukums)


def merki():
    global i
    for i in range(x):
        while True:
            merkaPozicija_x = random.randint(0, x-1)
            merkaPozicija_y = random.randint(0, y-1)
            if laukums[merkaPozicija_x][merkaPozicija_y] != "x":
                laukums[merkaPozicija_x][merkaPozicija_y] = "x"
                break

def laukuma_izvade(): #izvada laukumu
    for i in range(len(redzamais_laukums)):
        for j in range(len(redzamais_laukums)):
            print(redzamais_laukums[i][j], end = "\t")
        print()
    time.sleep(0.5)

def minesana(): #pieprasa lietotājam x un y vērtības minējumus
    global minejums_x, minejums_y
    while True:    
        minejums_x = input(f"Miniet punkta x koordināti no 0 līdz {x-1}: ")
        time.sleep(0.5)
        try:
            minejums_x = int(minejums_x)
            if minejums_x in range(0, x):
                break
            elif minejums_x > x: 
                print("Ievadīta pārāk liela vērtība, atceries, ka koordinātas var būt tikai veseli skaitļi, kuri ir vienādi/lielāki par 0. Lūdzu mēģiniet vēlreiz!")
            elif minejums_x < 0:
                print("Ievadīta pārāk maza vērtība, atceries, ka koordinātas var būt tikai veseli skaitļi, kuri ir vienādi/lielāki par 0. Lūdzu mēģiniet vēlreiz!")
                time.sleep(0.5)
        except ValueError:
            print("Ievadītā vērtība nav skaitlis, atceries, ka koordinātas var būt tikai veseli skaitļi, kuri ir vienādi/lielāki par 0. Lūdzu mēģiniet vēlreiz!")
            time.sleep(0.5)
    while True:
        minejums_y = input(f"Miniet punkta y koordināti no 0 līdz {y-1}: ")
        time.sleep(0.5)
        try:
            minejums_y = int(minejums_y)
            if minejums_y in range(0, y):
                break
            elif minejums_y > y: 
                print("Ievadīta pārāk liela vērtība, atceries, ka koordinātas var būt tikai veseli skaitļi, kuri ir vienādi/lielāki par 0. Lūdzu mēģiniet vēlreiz!")
            elif minejums_y < 0:
                print("Ievadīta pārāk maza vērtība, atceries, ka koordinātas var būt tikai veseli skaitļi, kuri ir vienādi/lielāki par 0. Lūdzu mēģiniet vēlreiz!")
                time.sleep(0.5)
        except ValueError:
            print("Ievadītā vērtība nav skaitlis, atceries, ka koordinātas var būt tikai veseli skaitļi, kuri ir vienādi/lielāki par 0. Lūdzu mēģiniet vēlreiz!")
            time.sleep(0.5)
        
def parbaude():
    if laukums[minejums_y][minejums_x] == "x":
        redzamais_laukums[minejums_y][minejums_x] = "x"
        print(f"Minējums x = {minejums_x}; y = {minejums_y} ir pareizs")
        time.sleep(0.5)
    else:
        print(f"Minējums x = {minejums_x} y = {minejums_y} ir nepareizs")
        time.sleep(0.5)
