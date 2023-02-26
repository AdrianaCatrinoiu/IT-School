#1. Scrieti o functie care returneaza reversul unei liste. Lista primita ca
# parametru nu trebuie modificata.

lista1 = [1,8,15,20]
#lista1.reverse()
lista2 = sorted(lista1, reverse=True)
print(lista1)
print(lista2)

#2. Scrieti o functie care returneaza True daca lista primita ca param. este 
# sortata, altfel returneaza False.
while lista1==lista1.sort():
    print(True)   
else:
    print(False)     

"""3. Scrieti o functie care primeste doua liste ca parametri. Listele contin numere intregi.
Fct. returneaza o singura lista formata din inmultirea dupa cum urmeaza: primul elem. din prima 
lista X primul elem. din a 2-a lista .... etc.
[1, 2, 3]
[3, 4, 6]
=> [3, 8, 18]"""

n = int(input("n = "))
lista3 =[]

for i in range(n):
    lista3.append(input())
    print(lista3)
print(lista3)






"""4) Create a mixed (sting and int) list with 10 elements
5) Print first and last element
6) Replace second element with 144
7) Print the index of element with value 144"""

list=["mere","pere",55,45]
print([0])

"""8) Make a function to remove all the element with a maximal value from a list; return a new list (original list does not modify)
9) Make a function for printing the first 5 longest strings in a list ; (len("test"))
10) Make a function to check if the elements of a lists are equals (without using for) -> return bool"""

