
import cv2
import matplotlib.pyplot as plt
import numpy as np



print("Zaczynamy zabawę z obrazkami w Pythonie.")


print("Wczytuję obrazek z komputera...")

nazwa_pliku_na_komputerze = "moja_cytryna.jpg"


obraz_oryginalny = cv2.imread(nazwa_pliku_na_komputerze)


if obraz_oryginalny is None:
    print(f"Nie mogę otworzyć pliku '{nazwa_pliku_na_komputerze}'.")
    print("Upewnij się, że plik istnieje i jest w tym samym katalogu co ten skrypt,")
    print("lub podaj pełną ścieżkę do pliku.")
    exit() 

print(f"Obrazek wczytany! Ma wymiary: {obraz_oryginalny.shape[1]} (szer.) x {obraz_oryginalny.shape[0]} (wys.).")


print("Pokazuję oryginalny obrazek.")

plt.figure(figsize=(8, 6))
plt.imshow(cv2.cvtColor(obraz_oryginalny, cv2.COLOR_BGR2RGB))
plt.title("Oryginalna Cytryna")
plt.axis('off')
plt.show() 


print("Zmniejszam i robię szary obrazek.")

wysokosc, szerokosc = obraz_oryginalny.shape[:2]
nowa_szerokosc = szerokosc // 2
nowa_wysokosc = wysokosc // 2

obraz_zmniejszony = cv2.resize(obraz_oryginalny, (nowa_szerokosc, nowa_wysokosc), interpolation=cv2.INTER_AREA)
obraz_szary = cv2.cvtColor(obraz_zmniejszony, cv2.COLOR_BGR2GRAY)

print(f"Obrazek jest teraz szary i ma wymiary: {obraz_szary.shape[1]} (szer.) x {obraz_szary.shape[0]} (wys.).")


print("\nKrok 4: Obracam obrazek o 90 stopni w prawo.")

obraz_obrocony = cv2.rotate(obraz_szary, cv2.ROTATE_90_CLOCKWISE)

print(f"Obrazek obrócony! Nowe wymiary: {obraz_obrocony.shape[1]} (szer.) x {obraz_obrocony.shape[0]} (wys.).")

print("\nPokazuję przetworzony obrazek.")

plt.figure(figsize=(6, 8))
plt.imshow(obraz_obrocony, cmap='gray')
plt.title("Cytryna: Zmniejszona, Szara i Obrócona")
plt.axis('off')
plt.show() 


print("\n---  Jak obrazek wygląda 'od środka' (jako liczby) ---")
print("\nFragment (10x10 pikseli) przetworzonego obrazka:")
print(obraz_obrocony[0:10, 0:10])

print(f"\nCały obrazek to taka tablica o rozmiarze : {obraz_obrocony.shape}")

print("To wszystko! ")