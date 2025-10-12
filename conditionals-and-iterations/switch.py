
day_number = int(input("Enter a day number (1-7): "))

if 1<= day_number <=5:
    print("It's a weekday")
elif day_number == 6:
    print("It's Saturday")
elif day_number == 7:       
    print("It's Sunday")
else:
    day = ''
    raise ValueError(
        str(day_number) + ' is not a valid day number.')