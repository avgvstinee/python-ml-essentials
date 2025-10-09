# implicit 

people = ['alice','bob','charlie','augustine']
ages = [60,70,35,25]
instruments = ['Guitar','Keyboard','Drums','Bass']

for data in zip(people,ages,instruments):
    person, age , instrument = data
    print(person,age,instrument)