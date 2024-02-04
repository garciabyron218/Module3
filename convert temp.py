#Byron Garcia
#will coonverts F to C
print('I will convert Fahrenheit to Celsius for you')
far_str = input('What is your temperature in Fahrenheit? ')
far = float(far_str)

celcius = (far - 32) * (5/9)
rounded_celcius = round(celcius, 2)

print('Your temperature is ' + str(rounded_celcius) + ' degrees Celsius')

if rounded_celcius < 5:
    print('Brrrr, that is cold')
elif rounded_celcius > 32:
    print('Hot!!')
