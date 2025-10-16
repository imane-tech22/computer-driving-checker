print('hello in our application')
city=input('please type your area to see if we can help you fix your computer in our selected regions')
city=city.strip().lower()
if city.lower()== 'casa':
    print ('we can help you ,please type your information')
elif city.upper()=='MARRAKECH':
    print('we can help you ,please type your information')
elif city.upper()== 'AGADIR':
    print('we can help you ,please type your information')
else:
    print('sorry , we can not help you because your area is not available')

print('the next:')
age=int(input('how old are you?'))

prm=input( 'do you have perme?')
prm=prm.strip().upper()
if age>= 18 and prm=='yes':
    print('you can drive ')
elif age<18 and prm=='no':
    print('you are not allowed to drive ')
elif age>=18 and prm=='no':
    print('you are allowed to drive but you cannot drive because you dont have perme')
else:
    print ( 'it is not logical to get perme and you are jut '+str(age) +' years old ' )





















