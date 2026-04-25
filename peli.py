import time

nimi = input("Anna lemmikille nimi: ")
nalka = 50
onni = 50
energia = 50

print(f"\n{nimi} on syntynyt!")

while nalka < 100 and energia > 0:
    print(f"\nNälkä: {nalka} | Onni: {onni} | Energia: {energia}")
    valinta = input("\n1: Ruoki, 2: Leiki, 3: Nuku, 4: Lopeta: ")
    
    if valinta == "1":
        nalka = max(0, nalka - 20)
        print("Mums!")
    elif valinta == "2":
        onni += 20
        energia -= 15
        print("Kivaa!")
    elif valinta == "3":
        energia = min(100, energia + 30)
        print("Zzz...")
    elif valinta == "4":
        break
    
    nalka += 5
    onni -= 5
    time.sleep(0.5)

print(f"\nPeli päättyi. {nimi} kaipaa lepoa.")
