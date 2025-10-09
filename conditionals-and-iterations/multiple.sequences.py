# Iterating over multiple sequences

people = ['alice','bob','charlie','augustine']
ages = [60,70,35,25]

for position in range(len(people)):
    person = people[position]
    age = ages[position]
    print(person,age)