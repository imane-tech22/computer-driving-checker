#Projet one
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

#Project two:

color=input('enter your first color that you really like ').lower()
more= input('do you want to add more colors : Yes or No?').lower()
if more=='yes':
    add_color=input("add another color to the list :").lower()
    colors=[]
    colors.append(color)
    colors.append(add_color)
    print(f'''the colors you like are:
{colors}''')
elif more=='no':
    print(f'your favorite color is {color}')
else:
    print('invalid option')


class_a=['ahmed','rim','sami','abd']
class_b=['rom','hani','sara']
all_courses=class_a+class_b
print(all_courses)


all=[]
all.extend(class_a)
all.extend(class_b)
print(all)

#Project three
import random
pin_ran=random.randint(1000,9999)
pin_if=input('enter 4 digits PIN code')
if pin_if==pin_ran:
    print('congratulations your code is correct')
elif len(pin_if)!=4:
    print('please enter 4 digits pin code')
elif len(pin_if)==4 and pin_if!=pin_ran:
    print(f'failure you entered this {pin_if } but the computer made this code {pin_ran}')
else:
    print ('invalid option')

#project four
import random
print('Welcome to whose wallet')
print('You will give me a list of names , and i will pick a person to pay')
names=input('If you get ready ,enter the names separated by a comma ')
list_name=names.split(', ')
random_list=random.randint(0,len(list_name)-1)
final_name=list_name[random_list]
print(f'please ask {final_name} to take his wallet out .DINNER ON HIM')

#two ways to solve

import random
names=input('''Welcome to whose wallet
You will give me a list of names , and i will pick a person to pay
If you get ready ,enter the names separated by a comma ''').split(', ')
print(f'please ask {random.choice(names)}to take his wallet out .DINNER ON HIM')


#project five:
basket=[['apples','bananas'],

        ['milk','water']]
print(basket)
enter=input('Press enter to change the context of the list ......')
basket[0].insert(0,'Oranges')
basket[0].insert(3,'Kiwis')
basket[1].remove('water')
basket[1].insert(0,'Coffee')
basket[1].append('tea')
basket.append(['1', '2','3'])
print(basket)

#project six:
print('welcome to place the rabbit')
list_one=[['☘','☘','☘'],['☘','☘','☘'],['☘','☘','☘']]
print(f'{list_one[0]}\n {list_one[1]}\n {list_one[2]}')
po=input('where should the rabbit go')
number_one=int(po[0])-1
number_two=int(po[1])-1
list_one[number_one][number_two]='🐇'
print(f'Success.....\n{list_one[0]}\n {list_one[1]}\n {list_one[2]}')

#projet seven:

print('welcome to the place of the rabbit')
way=['🌻','🌻','🌻'],['🌻','🌻','🌻'],['🌻','🌻','🌻']
print(f'{way[0]}\n{way[1]}\n{way[2]}')
go=input('''where should the rabbit go?
Please choose a row and a column''')
row=int(go[0])-1
column=int(go[1])-1
way[row][column]='🐇'
print(f'{way[0]}\n{way[1]}\n{way[2]}')

#project eight:

print('welcome to our stone iland')
stone=['💀','💀','💀','💀','💀'],['💀','💀','💀','💀','💀'],['💀','💀','💀','💀','💀'],['💀','💀','💀','💀','💀'],['💀','💀','💀','💀','💀']
print(f'{stone[0]}\n{stone[1]}\n{stone[2]}\n{stone[3]}\n{stone[4]}')
row_one=3
column_one=4
hide=input('''guess where is the money?
Please choose a row and a column''')
row=int(hide[0])-1
column=int(hide[1])-1
stone[row][column]='💰'

while row!=row_one or column!=column_one:
    print(f'''that is false :{hide}
try again''')
    hide = input('''guess where is the money?
    Please choose a row and a column''')
print(f'''congrats! you found the money 🤑
{stone[0]}\n{stone[1]}\n{stone[2]}\n{stone[3]}\n{stone[4]}''')

#Projet nine:
name=input ('Enter the first name and the last name of your friends separated by a comma').split(',')
listy=[]
for i in name:
    lists=i.split()
    print(lists)
    join='.'.join([lists[0][0].upper(),lists[-1][0].upper()])+'.'
    listy.append(join)
print('Abbreviated Names:')
print('\n'.join(listy))
#project ten:

# التمرين الأول: آخر حرف من الاسم الأول + الأخير
nom = input('Enter the first name of your friends separated by a comma: ').split(',')
letters = []

for name in nom:
    name = name.strip()  # إزالة المسافات الزائدة من البداية والنهاية
    words = name.split()
    if len(words) >= 2:  # للتأكد من وجود اسم أول واسم أخير
        abbrev = '.'.join([words[0][-1], words[-1][-1]])
        letters.append(abbrev)

print('Abbreviated Names:')
print('\n'.join(letters))

#Projet eleven:
# التمرين الثاني: أول حرف من الاسم الأول + أول حرف من الاسم الأخير + عدد الأصدقاء
nom_two = input('Enter the first name of your friends separated by a comma: ').split(',')
letters_two = []

for name in nom_two:
    name = name.strip(' ,!.@#$%^&*()_-+=?/\"')  # تنظيف الرموز من البداية والنهاية
    words = name.split()
    if len(words) >= 2:
        abbrev = '.'.join([words[0][0], words[-1][0]])
        letters_two.append(abbrev)

print('Abbreviated Names:')
print('\n'.join(letters_two))

numbers = len(nom_two)
print(f'You have {numbers} friends in your list')


#projet twelve:
test=input('enter a sentence:').split()
opposite=test[-1:-1000000:-1]
join=' '.join(opposite)
print(f' reversed sentence: {join}')



#project thirteen:
import string
sentence=input("Enter a sentence: ")
r=''
for word in sentence:
    if word not in string.punctuation:
        r+=word
print(r)

#Project fourteen:
print('hello world')
numbers=input('enter numbers separated by comma').split(',')
number=int(input('which number you want to negative ?'))
for i in numbers:
    number-=int(i)
    print(i)
    print(f' is {i}')

#Project fifteen
import random
number_1=int(input('Guess a number between 1 and 10: '))
secret_number=random.randint(1,10)
while number_1 != secret_number:
    if  number_1 < secret_number:
        number_1=int(input('That is too low! Guess again: '))
    elif number_1>secret_number:
        number_1=int(input('That is too high! Guess again: '))
    else:
        number_1=int(input('invalid input! Please Guess a number between 1 and 10: : '))
print(f'You guessed the secret number {secret_number}!')










