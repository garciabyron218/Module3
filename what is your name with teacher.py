#Byron Garcia
#program that will ask user for their full name then it will greet them by name if the correct name

user_name = input('What is your full name?')
teacher_name = 'Nathan Braun'
my_name = 'Byron Garcia'

if user_name == my_name:
    print('welcome' , user_name)

elif user_name == teacher_name:
    print ('Welcome' , teacher_name)

elif user_name != my_name or teacher_name:
    print ('Access Denied')


