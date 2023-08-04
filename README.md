# Collatzova_konvergencia_python
Collatzova konvergencia napisana v Python 3.10

[Collatzova konjugcia](https://en.wikipedia.org/wiki/Collatz_conjecture) [link](https://blog.sme.sk/teicher/veda-a-technika/collatzov-hlavolam-v-cislach-je-poriadok) je doposial nerozlustena matematicka hadanka ktora nam vravi ze vzdy ked opakujeme dve jednoduche matematicke operacie  tak prejdeme kazde pozityvne cislo pokial nedosiahneme 1.
Vypocet prebieha nasledovne:

  1. Zvoli sa lubovlne prirodzene cislo vacsie ako 0
  
  2. Ak je neparne vypocita sa kolko je s pouzitim vyrazu m = 3x + 1
  
  3. Ak je parne vypocita sa ako m = n/2
  
  4. Ak vysledok nema hodnotu tak je vlozeny do druheo kraku a pokus sa opatovne opakuje pokial nedosiahneme hodnotu 1

V tomto programe pouzivatel zada pozadovane cislo a nasledne program zacne pouzivat predchadzajuce podmienky na to aby toto cislo po case dostal na hodnotu 1
