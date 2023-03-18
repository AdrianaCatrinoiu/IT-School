#1. Creati un program care sa afiseze numele si prenumele vostru intr-un string folosind .format()
nume="Adriana Catrinoiu"
print( "Numele si prenumele:{}".format(nume))

#2. Creati un program care sa ceara utilizatorului numele si varsta, si sa afiseze un mesaj de salut personalizat.

nume_utiliz = input("Name:")
varsta_utiliz = input("Varsta")
print("Hello {}! You are {} years old?".format(nume_utiliz,varsta_utiliz))

#3. Creeaza o lista de cumparaturi cu cateva elemente in ea. (lista de stringuri).
#Creeaza un string formatat pentru a afisa ceva asemanator cu : Azi trebuie sa cumperi: mere, pere, struguri.


cumparaturi = ["mere", "pere", "struguri", "zahar", "faina"]
print("Astazi trebuie sa cumperi urmatoarele fructe: {}.".format(", ".join(cumparaturi)))


#4. Creati un program care sa afiseze
    
""" $
   ***
  *****
 *******
********* """