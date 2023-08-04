
import time

#ziskanie pociatocneho cisla
while True:
    print("Vloz pociatocne cislo: ")
    odpover = input()
    #uistenie sa ze je to cislo
    if odpover.isdecimal():
        break
    else:
        print("Musis vlozit cele cislo vacsie ako 0")
    
n = int(odpover)
print(n, end = "", flush=True)
while n != 1:
    #urcenie ci sa jedna o parne alebo neparne cislo
    #parne
    if n % 2 == 0:
        n = n//2
    #neparne
    else:
        n = 3*n + 1

    #ak print() neobsahuje flush=True dochadza k tomu ze sa vypluje vsetko naraz a nie postupne ako ked obsahuje flush=true, end="" osetruje to aby sa text zobrazoval za sebou a nie aby sa pisal do noveho riadky ako je to ked sa napise print(). V tedy dochadza k tomu ze sa dalsi print vypise do noveho riadku. Ked je tato hodnota zmene tak sa vypisuje za sebou
    print(", " +str(n), end = "")
    #sposobuje to ze sa vypisovanie textu vypisuje postupne a nie naraz po vypocte
    time.sleep(0.1)
print()