#ex cu dictionare fara cele cu functii

"""1. Creați o listă cu patru tuple, fiecare tuplă conținând numele
și vârsta unui angajat. Convertiți lista într-un dicționar unde
cheia este numele angajatului și valoarea este vârsta acestuia."""

angajati = [("Ionescu Maria", 45 ),("Popescu Ion", 54),("Popa Mihai", 35),("Anghel Diana", 25)]
dictionar_angajati = {}

for i in angajati:
    dictionar_angajati[i[0]]=[i[1]]

print(dictionar_angajati)


#2.

centraliz_angajati = [

    {"numele":"Ion","varsta":45, "salariu":6500},

    {"numele":"Maria","varsta":35, "salariu":4500},

    {"numele":"Marius","varsta":26, "salariu":2500},

    {"numele":"Cristina","varsta":37, "salariu":3500},

    ]

 

print(centraliz_angajati)

 

for i in centraliz_angajati:

    print(i["numele"], i["salariu"])

 

#3 Creați un dicționar cu numele și nota a patru studenți. Adăugați o

#nouă intrare în dicționar pentru un nou student și actualizați nota unui

#student existent. Afișați numele studenților si nota in ordine alfabetică.

 

students_grades = {

    'Ana': 9.5,

    'Ioan': 8.0,

    'Maria': 7.5,

    'Andrei': 9.0,

}

 

students_grades['Irina']= 10

students_grades.update({"Andrei": 6.0})

print(students_grades)

 

 

#5. Creați o listă cu cinci dicționare, fiecare dicționar conținând numele și

#notele unui student. Iterați prin lista și calculați media notelor fiecărui

#student. Adăugați media ca o intrare suplimentară în fiecare dicționar.

#Sortați lista în funcție de medie și afișați numele și nota fiecărui student

#în ordine crescătoare a mediilor.

 

a = [

    {

        "nume": "Elena",

        "note": [4, 5, 6]

    }

]

 

 

lista_student = [

    {"numele":"Ion","nota":[8.0,7,6]},

    {"numele":"Maria","nota":[9.5,4,9]},

    {"numele":"Marius","nota":[9.0,10,9]},

    {"numele":"Cristina","nota":[8.3,10,7]},

    {"numele":"Irina","nota":[6.5,8,9]},

    ]

   

medie = sum(student["nota"]) / len(student["nota"])

   

for student in lista_student:

    student["medie"] = sum(student["nota"]) / len(student["nota"])

   

print(lista_student)

 

 

rezultate_campionat = [

    {"echipa": "CFR Cluj", "meciuri_jucate": 36, "victorii": 22, "egaluri": 9, "infrangeri": 5},

    {"echipa": "FCSB", "meciuri_jucate": 36, "victorii": 21, "egaluri": 7, "infrangeri": 8},

    {"echipa": "Universitatea Craiova", "meciuri_jucate": 36, "victorii": 18, "egaluri": 11, "infrangeri": 7},

    {"echipa": "Sepsi Sfântu Gheorghe", "meciuri_jucate": 36, "victorii": 15, "egaluri": 11, "infrangeri": 10},

    {"echipa": "Astra Giurgiu", "meciuri_jucate": 36, "victorii": 14, "egaluri": 11, "infrangeri": 11},

    {"echipa": "CS Mioveni", "meciuri_jucate": 36, "victorii": 13, "egaluri": 12, "infrangeri": 11},

    {"echipa": "FC Argeș Pitești", "meciuri_jucate": 36, "victorii": 13, "egaluri": 9, "infrangeri": 14},

    {"echipa": "FC Botoșani", "meciuri_jucate": 36, "victorii": 12, "egaluri": 10, "infrangeri": 14},

    {"echipa": "Gaz Metan Mediaș", "meciuri_jucate": 36, "victorii": 11, "egaluri": 12, "infrangeri": 13},

    {"echipa": "FC Voluntari", "meciuri_jucate": 36, "victorii": 12, "egaluri": 8, "infrangeri": 16},

    {"echipa": "Academica Clinceni", "meciuri_jucate": 36, "victorii": 10, "egaluri": 12, "infrangeri": 14},

    {"echipa": "FC Hermannstadt", "meciuri_jucate": 36, "victorii": 10, "egaluri": 11, "infrangeri": 15}

]

 

#avand in vedere ca o victorie valoreaza 3 pct. si un egal 1 pct.

#a) sa se adauge o cheie noua in fiecare dictionar, numele cheii este 'puncte'

#iar ca valoare va avea numarul de puncte acumulate

