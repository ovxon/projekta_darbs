import time

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