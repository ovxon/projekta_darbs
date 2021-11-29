import random
import time

grutibas_limenis = 0
laukums = []
redzamais_laukums = []
rezultats = []
laukuma_kopija = []
merkaPozicija_x = 0
merkaPozicija_y = 0
merku_skaits = 0
minejumu_skaits = 0
punkti = 0
vards = 0
izvele = 0
mape = "faili/"

def limena_izvele(): #pieprasa lietotājam grūtības līmeni
    global grutibas_limenis
    while True:
        grutibas_limenis = input("Izvēlieties grūtības līmeni no 1-3 (1 ir visvieglākais, 3 - visgrūtākais): ")
        time.sleep(0.5)
        try:
            grutibas_limenis = int(grutibas_limenis)
            if grutibas_limenis in range(1, 4):
                break
            else: 
                print("Ievadīta pārāk liela vērtība, mēģiniet vēlreiz")
                time.sleep(0.5)
        except ValueError:
            print("Ievadītā vērtība nav skaitlis, mēģiniet vēlreiz")
            time.sleep(0.5)

def laukuma_izmeri(): #aprēķina spēles lauka izmērus
    global x, y
    x, y = grutibas_limenis + 2, grutibas_limenis + 2

def laukuma_izveide(x, y): #izveido laukumu
    global laukums
    global redzamais_laukums
    global laukuma_kopija
    laukums = [["o" for i in range(x)] for j in range(y)]
    laukums = tuple(laukums)
    redzamais_laukums = [["o" for i in range(x)] for j in range(y)]
    laukuma_kopija = tuple(laukums)

def merki(): #ģenerē mērķu pozīcijas un pievieno mērķus laukumam
    global merkaPozicija_x, merkaPozicija_y
    for i in range(x):
        while True:
            merkaPozicija_x = random.randint(0, x-1)
            merkaPozicija_y = random.randint(0, y-1)
            if laukums[merkaPozicija_x][merkaPozicija_y] != "x":
                laukums[merkaPozicija_x][merkaPozicija_y] = "x"
                break

def laukuma_izvade(): #izvada laukumu teksta formā
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
            else:
                print("Ievadīta pārāk liela vērtība, mēģiniet vēlreiz")
                time.sleep(0.5)
        except ValueError:
            print("Ievadītā vērtība nav skaitlis, mēģiniet vēlreiz")
            time.sleep(0.5)
    while True:
        minejums_y = input(f"Miniet punkta y koordināti no 0 līdz {y-1}: ")
        time.sleep(0.5)
        try:
            minejums_y = int(minejums_y)
            if minejums_y in range(0, y):
                break
            else: 
                print("Ievadīta pārāk liela vērtība, mēģiniet vēlreiz")
                time.sleep(0.5)
        except ValueError:
            print("Ievadītā vērtība nav skaitlis, mēģiniet vēlreiz")
            time.sleep(0.5)

def parbaude(): #pārbauda vai ievadītās koordinātas sakrīt ar kāda mērķa koordinātām
    if laukums[minejums_y][minejums_x] == "x":
        redzamais_laukums[minejums_y][minejums_x] = "x"
        print(f"Minējums x = {minejums_x}; y = {minejums_y} ir pareizs")
        time.sleep(0.5)
    else:
        print(f"Minējums x = {minejums_x} y = {minejums_y} ir nepareizs")
        time.sleep(0.5)

def programmas_darbiba(): #izpilda visas funkcijas pareizā secībā
    while True:
        global minejumu_skaits
        global punkti
        global izvele
        global vards
        global rezultats
        global mape
        global rezultatu_izvele
        minejumu_skaits = 0
        punkti = 0
        rezultats = []
        while True:
            izvele = input("Vai vēlaties sākt jaunu spēli? Ja jā - ievadiet 0, ja nē - ievadiet 1: ")
            time.sleep(0.5)
            try:
                izvele = int(izvele)
                if izvele == 1:
                    print("Paldies par programmas izmantošanu")
                    break
                elif izvele == 0:
                    break
                else:
                    print("Ievadītā vērtība nav derīga, mēģiniet vēlreiz")
                    time.sleep(0.5)
            except ValueError:
                print("Ievadītā vērtība nav skaitlis, mēģiniet vēlreiz")
                time.sleep(0.5)
        if izvele == 1:
            break
        limena_izvele()
        laukuma_izmeri()
        laukuma_izveide(x, y)
        merki()
        while True:
            laukuma_izvade()
            minesana()
            minejumu_skaits += 1
            parbaude()
            if laukums[minejums_y][minejums_x] == "x":
                punkti += 1
                laukums[minejums_y][minejums_x] = "o"
            print(f"Minējumu skaits: {minejumu_skaits}")
            print(f"Punktu skaits: {punkti}")
            if punkti == x:
                break
        vards = str(input("Kāds ir jūsu vārds? "))
        rezultats = [vards, grutibas_limenis, punkti, minejumu_skaits]
        print(f"Vārds: {vards}, grūtības līmenis: {grutibas_limenis}, {chr(112) + chr(117) + chr(110) + chr(107) + chr(116) + chr(105)}: {punkti}, minējumu skaits: {minejumu_skaits}")
        f = open(mape + "rezultati.txt", "a")
        f.write(str(rezultats))
        f.write("\n")
        f.close()
        while True:
            rezultatu_izvele = input("Vai vēlaties redzēt visus iepriekšējos rezultātus? (Ievadiet 0 - ja jā, un 1 - ja nē) )")
            try:
                rezultatu_izvele = int(rezultatu_izvele)
                if rezultatu_izvele == 0:
                    print("Visi rezultāti:")
                    l = open(mape + "rezultati.txt", "r")
                    print(l.read())
                    break
                elif izvele == 1:
                    break
                else:
                    print("Ievadītā vērtība nav derīga, mēģiniet vēlreiz")
                    time.sleep(0.5)
            except ValueError:
                print("Ievadītā vērtība nav skaitlis, mēģiniet vēlreiz")
                time.sleep(0.5)

programmas_darbiba()
