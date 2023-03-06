#1. Creați un dicționar care să conțină numele și vârsta a trei persoane.

#Apoi, iterați prin dicționar și afișați numele și vârsta fiecărei persoane.

 

persoane = {"Alex": 25, "Maria": 30, "Andrei": 21}

for k,v in persoane.items():

    print(k,v)

#2. Creați un dicționar cu numele și notele a trei studenți.

#Calculați media notelor și afișați-o alaturi de numele studentului.

 

students_grades = {

    'Ana': [9.5,10,8],

    'Ioan': [8.0,10,5],

    'Maria': [7.5,9.0,4],

    }

 

 

for k,v in students_grades.items():

    print(k,sum(v)/len(v))

   

 

#3. Creați un dicționar cu numele și salariul a trei angajați.

#Afișați salariatul cu cel mai mare salariu.

persoane1= {"Alex": 2500, "Maria": 3000, "Andrei": 2100}

 

 

max_salariu = max(persoane1.keys())

print(max_salariu )

 

#sau

 

 

sorted_values = sorted(persoane1.values())

sorted_dict = {}

for i in sorted_values:

    for k in persoane1.keys():

        if persoane1[k] == i:

            sorted_dict[k] = persoane1[k]

           

max_salariu = max(persoane1.keys())

print(max_salariu)

 

 

#4. Creați un dicționar cu numele și data de naștere a trei persoane.

#Adăugați o nouă persoană la dicționar și afișați numele și data de naștere a

#tuturor persoanelor.

persoane2= {"Alex": '25-01-2008', "Maria": '01-01-1988', "Andrei": '18-06-1991'}

persoane2["Marius"] = '06-06-1988'

print(persoane2)

 

for k,v in persoane2.items():

    print(k,v)

 

 

#5. Creați un dicționar cu numele și adresa a trei prieteni.

#Modificați adresa celui de-al doilea prieten și afișați dicționarul actualizat.

 

persoane_adress= {"Alex": 'str Unirii nr 3', "Maria": 'str Rucar nr22', "Andrei": 'str Titulescu nr 15'}

persoane_adress["Maria"] = 'str Vatra Dornei'

print(persoane_adress)

 

#6. Creați un dicționar cu numele și vârsta a trei persoane.

#Ștergeți persoana cu vârsta cea mai mică și afișați dicționarul actualizat - de intrebat.

 

employee = {"Alex": 25, "Maria": 30, "Andrei": 21}

 

min_age = 999

min_age_name = ""

 

for name, age in employee.items():

    if age < min_age:

        min_age = age

        min_age_name = name

 

del employee[min_age_name]

 

print(employee)

#7. Creați un dicționar cu numele și ocupația a cinci persoane.

#Apoi, utilizați un buclă "for" pentru a itera prin dicționar și afișați numele

#și ocupația fiecărei persoane.

 

#8. Creați un dicționar cu numele și numărul de telefon a trei prieteni.

#Afișați numerele de telefon în ordine alfabetică a numelor.

 

#9. Creați un dicționar cu numele și nota a cinci studenți.

#Afișați numele studentului cu cea mai mare notă.

 

#10. Creați un dicționar cu numele și vârsta a patru persoane.

#Sortați dicționarul în funcție de vârstă și afișați numele și vârsta

#fiecărei persoane în ordine crescătoare de vârstă.

 

#11. Creați un dicționar cu numele și notele a patru studenți.

#Afișați numele și media fiecărui student în ordine descrescătoare a mediei.