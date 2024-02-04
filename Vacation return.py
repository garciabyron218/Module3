#Byron Garcia
#2/2/24
#Program will figure out what day youll be back

day_dict = {
    "Sunday":0,
    "Monday":1,
    "Tuesday":2,
    "Wednesday":3,
    "Thursday":4,
    "Friday":5,
    "Saturday":6,}

leave_day_str = (input("what day do you leave? "))
leave_day = day_dict.get(leave_day_str.title(), -1)

if leave_day == -1:
    print("Invalid input")
    

else:
    Length_days = int(input("How many days will you be gone?"))
    return_day_number = (leave_day + Length_days) % 7
    return_day = [key for key, value in day_dict.items() if value == return_day_number][0]
    print("You will return ", return_day)
