import random
import time
import moduli as mod

merku_skaits, minejumu_skaits, punkti, vards, izvele = 0, 0, 0, 0, 0
mape = "faili/"

def main_darbiba(): #izpilda visas funkcijas pareizā secībā
    while True:
        global minejumu_skaits, punkti, izvele, vards, mape, minejumu_skaits, rezultatu_izvele, rezultatu_saraksts
        minejumu_skaits, punkti = 0, 0
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
        mod.limena_izvele()
        mod.laukuma_izveide()
        mod.merki()
        while True:
            mod.laukuma_izvade()
            mod.minesana()
            minejumu_skaits += 1
            mod.parbaude()
            if mod.laukums[mod.minejums_y][mod.minejums_x] == "x":
                punkti += 1
                mod.laukums[mod.minejums_y][mod.minejums_x] = "o"
            print(f"Minējumu skaits: {minejumu_skaits}")
            print(f"Punktu skaits: {punkti}")
            if punkti == mod.x:
                mod.laukuma_izvade()
                break
        vards = str(input("Kāds ir jūsu vārds? "))
        rezultatu_saraksts = {
            "Vārds": vards,
            "Grūtības līmenis": mod.grutibas_limenis,
            "Punkti": punkti,
            "Minējumi": minejumu_skaits
        }
        print(f"Vārds: {vards}, grūtības līmenis: {mod.grutibas_limenis}, {chr(112) + chr(117) + chr(110) + chr(107) + chr(116) + chr(105)}: {punkti}, minējumu skaits: {minejumu_skaits}")
        f = open(mape + "rezultati.txt", "a")
        f.write(str(rezultatu_saraksts))
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