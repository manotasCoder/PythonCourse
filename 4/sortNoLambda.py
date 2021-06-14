people = [
    {'name': "Harry", 'house': 'Griffindor'},
    {'name': "Cho", 'house': 'Ravenclaw'},
    {'name': "Draco", 'house': 'Slytherin'}
]

def f(person):
    return person["name"]

people.sort(key=f)


print(people)