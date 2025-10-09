# expanding little more on multiple.sequences.zip.py
# explicit

people = ['alice','bob','charlie','augustine']
ages = [60,70,35,25]
instruments = ['Guitar','Keyboard','Drums','Bass']

for person , age , instrument in zip(people,ages,instruments):
    print(person,age,instrument)