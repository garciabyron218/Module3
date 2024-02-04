#Byron Garcia
#2/2/24
#Program will calcualte MPG
print('I will calculate miles per gallon for you')
miles_str = input('How many miles did you drive? ')
miles = float(miles_str)

gallons_str = input('How many gallons of gas did you use? ')
gallons = float(gallons_str)
    
mpg = miles / gallons
print('Your car has a mpg of ' +str(mpg))


