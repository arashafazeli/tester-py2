#calculate the volume of an equilateral cube and an equilateral tetrahedron
a = float(input('what objects volume do you want to calculate? 1.cube 2.tetrahedron :'))
side = float(input('please enter length of any side of equilateral cube or tetrahedron in cm:'))
#calculate the volume of an equilateral cube
v1= side**3
#calculate the volume of an equilateral tetrahedron
v2= (side**3) / (6*1.4142138)
#create a list that contains the volum of cub and tetrhedron
x= [0,v1,v2]
#use slicing to creat volume
v = x[int(a)]
#print out volume
print ('The volume is: '+ str(v)+' ㎤')

