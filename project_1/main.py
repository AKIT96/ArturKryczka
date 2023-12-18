import matplotlib.pyplot as plt
import numpy as np
import random
import os
from datetime import datetime

#Zadanie_1
def ex_1():
    for liczba in range(1, 101):
        if liczba % 3 == 0 and liczba % 5 == 0:    #Liczba podzielna przez 3 i 5 --> "FizzBuzz"
            print("FizzBuzz")
        elif liczba % 3 == 0:        #Liczba podzielna przez 3 --> "Fizz"
            print("Fizz")
        elif liczba % 5 == 0:        #Liczba podzielna przez 5 --> "Buzz"
            print("Buzz")
        else:
            print(liczba)

#Miejsce na wywołanie funkcji:
ex_1()



#Zadanie_2
def ex_2(n):
    with open("losowe_liczby.txt", "w") as plik:        #Tworzenie pliku: "losowe_liczby.txt"
        for losowe_liczby in range(n):
            liczba = random.randint(1, 100)        #Liczby do wylosowania
            plik.write(str(liczba) + "\n")        #Zapis każdej liczby w pliku txt od nowej linii
            print(liczba)

n = int(input("Podaj wartość liczby n: "))

#Miejsce na wywołanie funkcji:
ex_2(n)



#Zadanie_3
def ex_3(losowe_liczby):
    with open(losowe_liczby, 'r') as plik:        #Odczytanie wcześniej zapisanego pliku
        liczby = [int(line.strip()) for line in plik]
    return liczby

#Średnia:
def liczenie_sredniej(liczby):
    suma = sum(liczby)
    ilosc = len(liczby)
    srednia = suma / ilosc
    return srednia

#Odchylenie standardowe:
def odchylenie_standardowe(liczby):
    srednia = liczenie_sredniej(liczby)
    suma_kwadratow_roznicy = sum((x - srednia) ** 2 for x in liczby)
    odchylenie = (suma_kwadratow_roznicy / len(liczby)) ** 0.5
    return odchylenie

#Wartość minimalna:
def wartosc_minimalna(liczby):
    minimalna_wartosc = min(liczby)
    return minimalna_wartosc

#Wartość maksymalna:
def wartosc_maksymalna(liczby):
    maksymalna_wartosc = max(liczby)
    return maksymalna_wartosc

#Liczby posortowane malejąco:
def sortowanie_malejaco(liczby):
    liczby.sort(reverse=True)
    return liczby

#Wszystkie obliczone wartości:
def wyniki(liczby):
    print("Średnia: ", liczenie_sredniej(liczby))
    print("Odchylenie standardowe: ", odchylenie_standardowe(liczby))
    print("Wartość minimalna: ", wartosc_minimalna(liczby))
    print("Wartość maksymalna: ", wartosc_maksymalna(liczby))
    print("Posortowane malejąco: ", sortowanie_malejaco(liczby))

#Miejsce na wywołanie funkcji:
liczby = ex_3("losowe_liczby.txt")
wyniki(liczby)



#Zadanie_4
def ex_4(n):
    fibonacci = [0, 1]

    for i in range(2, n):
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return fibonacci

#Prośba o podanie wartości n dla ciągu Fibonacciego przez użytkownika
n = int(input("Podaj liczbę n dla ciągu Fibonacciego: "))

def zapisanie_pliku(plik_z_danymi, dane):
    with open(plik_z_danymi, 'w') as plik:
        for wiersz in dane:
            plik.write("%s\n" % wiersz)

#Miejsce na wywołanie funkcji:
gen_fibonacci = ex_4(n)

#Zapisanie liczb do pliku aby wygenerować wykres z zadania 5
zapisanie_pliku("fibonacci.txt", gen_fibonacci)
print(gen_fibonacci)



#Zadanie_5
def ex_5(odczytanie_pliku):
    with open(odczytanie_pliku, 'r') as plik:
        fibonacci = [int(wiersz.strip()) for wiersz in plik]

    n = len(fibonacci)
    plt.plot(range(1, n + 1), fibonacci, marker='o', linestyle='-', color='b')
    plt.title(f'Ciąg Fibonacciego dla n={n}')
    plt.xlabel('Liczba')
    plt.ylabel('Wartość')
    plt.grid(True)
    plt.show()

#Miejsce na wywołanie funkcji:
ex_5("fibonacci.txt")



#Zadanie_6
def ex_6(n):
    słownik = {}
    for x in range(1, n+1):        #Generowanie liczb w słowniku
        słownik[x] = x**2        #Podniesienie wartości ze słownika do kwadratu
    print(słownik)
    return słownik
n = int(input("Podaj wartość n: "))

#Miejsce na wywołanie funkcji:
gen_słownik = ex_6(n)



#Zadanie_7
def ex_7(słownik):
    suma = sum(słownik.values())            #Zsumowanie wartości słownika
    print("Suma wartości słownika:", suma)

#Miejsce na wywołanie funkcji:
#Aby funkcja zsumowała wartości ze słownika trzeba odnieść się do funkcji z zadania 6
ex_7(gen_słownik)



#Zadanie_8
def ex_8():
    #Utworzenie folderu z 10 plikami
    nazwa_folderu = "Pliki do zadania 8"
    if not os.path.exists(nazwa_folderu):
        os.makedirs(nazwa_folderu)

    #Generowanie nazwy pliku na podstawie daty i godziny
    for plik in range(10):
        data = datetime.now().strftime("%Y_%m_%d_%H_%M_%S_%f")
        pliki = os.path.join(nazwa_folderu, f"{data}.bin")

        #Wygenerowane losowe dane
        dane = bytes([random.randint(0, 255) for losowe_dane in range(1024)])        #Rozmiar danych

        #Zapisane dane do pliku binarnego
        with open(pliki, 'wb') as plik:
            plik.write(dane)

#Funkcja aby komunikat wyświetlał sie raz a nie 10 razy
def wyswietlenie_tekstu_raz():
    if not hasattr(wyswietlenie_tekstu_raz, "wyświetlono"):
        print("Utworzono plik do zadania 8.")
        wyswietlenie_tekstu_raz.wyświetlono = True

#Miejsce na wywołanie funkcji:
wyswietlenie_tekstu_raz()
ex_8()



#Zadanie_9
def ex_9(url):
    #Pobranie danych z pliku CSV
    dane = pd.read_csv(url)

    #Wykresy
    fig, axs = plt.subplots(3, 1, figsize=(10, 12), sharex=True)

    axs[0].plot(dane['time_from_start'], dane['pos_x'], label='pos_x', color='r')
    axs[0].set_ylabel('Position X')

    axs[1].plot(dane['time_from_start'], dane['pos_y'], label='pos_y', color='b')
    axs[1].set_ylabel('Position Y')

    axs[2].plot(dane['time_from_start'], dane['pos_z'], label='pos_z', color='g')
    axs[2].set_ylabel('Position Z')

    plt.xlabel('time_from_start')
    plt.show()

    #Obliczenie średnich pozycji
    Pozycja_x = np.mean(dane['pos_x'])
    Pozycja_y = np.mean(dane['pos_y'])
    Pozycja_z = np.mean(dane['pos_z'])

    print(f"Średnia pozycja X: {Pozycja_x}")
    print(f"Średnia pozycja Y: {Pozycja_y}")
    print(f"Średnia pozycja Z: {Pozycja_z}")

    #Obliczanie prędkości i zapisywanie do pliku CSV
    dane['velocity'] = np.sqrt(dane['vel_x']**2 + dane['vel_y']**2 + dane['vel_z']**2)
    dane[['velocity']].to_csv('velocity.csv', index=False)

    print("Prędkości zostały zapisane do pliku 'velocity.csv'.")

#Miejsce na wywołanie funkcji:
url = "https://raw.githubusercontent.com/uzh-rpg/agile_autonomy/958c0d22e11d28a4d73b627029cf62ef1a1a95ab/data_generation/viz_utils/pole_avoidance/reference_trajectory.csv"
ex_9(url)


def main():
    ex_1()
    ex_2()
    ex_3()
    ex_5()
    ex_6()
    ex_7()
    ex_8()
    ex_9()

if __name__ == '__main__':
    main()
