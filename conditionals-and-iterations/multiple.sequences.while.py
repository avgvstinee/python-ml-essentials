# multiple sequences with while loop

people = ['alice', 'bob', 'charlie', 'augustine']
ages = [60, 70, 35, 25]

position = 0
while position < len(people):
    person = people[position]
    age = ages[position]
    print(person, age)
    position += 1
# Output:
# alice 60
# bob 70
# charlie 35
# augustine 25
