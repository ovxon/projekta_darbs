import random
import time
import moduli as mod

rezultats = []
merku_skaits = 0
minejumu_skaits = 0
punkti = 0
vards = 0
izvele = 0
mape = "faili/"


mod.limena_izvele()

mod.laukuma_izveide()

mod.merki()

mod.laukuma_izvade()

mod.minesana()

mod.parbaude()

def main_darbiba(): #izpilda visas funkcijas pareizā secībā
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

main_darbiba()