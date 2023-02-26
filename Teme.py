
# 7. Scrie un program care citeste de la tastatura un nr. natural
# si verifica daca acesta este palindrom. 111 121 292 2992 33533


num=int(input("number:"))

nr2=num
rev=0
while(num>0):
    dig=num%10
    rev=rev*10+dig
    num=num//10
if(nr2==rev):
    print("True")
else:
    print("False")


# 8. Scrie un program care calculeaza care este
# dimesiunea optima a unei placi de gresie astfel in cat sa se poata
# placa o camera cu dimensiunea 21 m x 6 m fara a taia din placa de gresie.
# NOTA: Placile de gresie au toate laturile egale.

a =21
b=6
while b:
    a=b
    b=a%b
print (a)
math.gcd(a,b)


# 1.Scrieti un program care afiseaza numerele prime din intervalul [0 100].
interv=range(0,101)

for n in interv :
    print (n)

#2. Scrieti un program care afiseaza numerele impare in intervalul [0, 1000]
interv=range (1,1001,2)

for n in interv :
    print (n)

for nr in range(0,1001):
    if nr %2==0:
        print("nr par",nr)
        continue
    print("nr impar",nr)
    
        

#3. Scrieti un program care citeste de la tastatura un nr natural "n", 
#si afiseaza suma primelor n numere multiple de 5 si 3


counter=0

for i in range (0,int(input()),5):   
    counter +=i
print(counter)


c=0
suma=0
while k<=5:
    if c %3==0 and c%5==0:
        suma +=c
        k +=1
        c +=1
print(suma)






#4. Scrieti un program care citeste de la tastatura un nr natural "n", 
#si afiseaza n! (factorial). 6! = 1 * 2 * 3 * 4 * 5 * 6

print("Introduceti un numar pentru a obtine factorialul: ")
 
factorial = 1
 
for i in range(1,int(input())+1):
    factorial *= i
 
print(f"Rezultatul este: {factorial}")


"""5. Scrieti un program care afiseaza toate litere (capitale) ale 
alfabetului englez, pe aceiasi linie despartite prin spatiu. 
**A se vedea tablelul ASCII. chr(65) -> A"""

