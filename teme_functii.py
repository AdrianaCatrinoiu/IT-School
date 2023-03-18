#1) Write a function to set None at a specified key in a dict


ticket = {
    "plecare": "Bucuresti Nord",
    "sosire": "Iasi",
    "data_plecare": "27.02.2023",
    "data_sosire": "27.02.2023",
    "ora_plecare": "19.30",
    "ora_sosire": "23.30",
    "pret": 98.45,
    "loc": 25,
    "vagon": "2",
    "scaun": "34",
}


def set_none_at_key(dictionary, key):
    """
    Sets a None value at the specified key in a dictionary.
    """
    dictionary[key] = None

set_none_at_key(ticket,'loc')

print(ticket)


#2) Remove all the items from months dict with value greater then 6
#use list comprehention

months = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 
          'June': 6, 'July': 7, 'August': 8, 'September': 9, 'October': 10,
            'November': 11, 'December': 12}

months = {k: v for k, v in months.items() if v <= 6}

print(months)

#4) Make list of dictionaries, each dictionaries contains the following attributes: name, age, gender;
#  Read those info from keyboard input.
#5) sort list by users age


user_list = []

# Ask the user to enter information for each user and add it to the list
while True:
    name = input("Enter the user's name (or 'done' to exit): ")
    if name == 'done':
        break
    age = int(input("Enter the user's age: "))
    gender = input("Enter the user's gender: ")
    user = {'name': name, 'age': age, 'gender': gender}
    user_list.append(user)


user_list.sort(key=lambda x: x['age'])
print(user_list)

#6) scrieti o functie (get_week_days) care returneaza un dictionar ce contine zilele saptamanii, mapate de forma "luni": 1
#functia trebuie sa primeasca un param. optional de tip bool (work_week) cu val default False;
#Daca work_week este adevarat atunci se va returna un dict. ce contine doar zilele lucratoare.

def get_week_days(work_week=False):
    weekdays = {
        1: 'Monday',
        2: 'Tuesday',
        3: 'Wednesday',
        4: 'Thursday',
        5: 'Friday',
        6: 'Saturday',
        7: 'Sunday'
    }
    
    if work_week:
        weekdays = {
            1: 'Monday',
            2: 'Tuesday',
            3: 'Wednesday',
            4: 'Thursday',
            5: 'Friday'
        }
    
    return weekdays

# Example usage:
#days_of_week = get_week_days()
#print(days_of_week)

work_days_only = get_week_days(work_week=True)
print(work_days_only)



