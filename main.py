print('hello world from\n Dr.krillzorz')
print('Now iam down here\n')
hello = 'This is a string inside a variable\n'
universe = 42
foo = '42'
bar = 1.25
space = ' '
d = 'world' ,bar

#print(hello)
#print(type(hello))


#print(world)
#print(type(world))


#print(foo)
#print(type(foo))


#print(bar)
#print(type(doob))
#print (bar+universe +int(foo))


hello = 'This is a string inside a variable'
universe = 42
bar = 1.25
foo = '42'
space = ' .:. '
 
# print(type(hello))
# print(type(world))
# print(type(d))
# print('hello' + space + 'world' + space + str(bar))
# print(type(bar))
 

#skriv en funktionsdefinition som tar in en parameter
#parametern består av en sträng som består av en fråga 
#funktionen ska stäla frågan till användaren
#det användaren svarar skall konverteras till int eller float
#samt retuneras tillbaka till anropande kod
def ask_user (prompt):
    #print('The funkytion was called with argument {prompt}')
    s = input(prompt)
    #print(type(s))
    return eval(s)


answer = ask_user('please enter a length in meters')
print(f'Then user answered {answer} ')

#s = eval(input('please enter a distance in cm: '))
#print(s)
#print(type(s))
#area = s ** 2
print('The area of a square with side ' + str(s) +
      ' cm is equal to ' + str(area) + ' cm^2')