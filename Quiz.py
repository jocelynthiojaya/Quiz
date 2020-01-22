# Multiple Choice

#7
print('7:')
str="hello" 
print(str[:2])
print('\n')

#8
print('8:')
x_8 = 13 // 2 #floor division, always roundup to left int
y_8 = int(13 / 2)
z_8 = 13 % 2 #modulo is the remainder. if 1st>2nd number, result is 1st.
print(x_8, y_8, z_8)
print('\n')

#9
print('9:')
def example(a):     
    a = a + '2'     
    a = a*2     
    return a 
print(example("hello"))
print('\n')

#13
print('13:')
def f(p, q):  
    return p%q 
print(f(0, 2))
# f(2, 0) is zerodivision error, cannot be divided by 0
print('\n')

#14
print('14:')
x_14 = ['ab', 'cd']
for i in x_14:   
    i.upper() #upper() doesnt really change anything diluar line dia
print(x_14)
print('\n')

#15
print('15:')
x_15 = ['ab', 'cd'] 
# for i in x_15:
    # x_15.append(i.upper())
    # this will make an endless loop
# print(x_15)
print('\n')

#16
print('16:')
# True = False 
# while True:     
    # print(True)     
    # break
print('cannot assign variable to True, ato apapun yg udh ada default')
print('\n')

#17
print('17:')
x_17 = "abcdef" 
i = "a" 
while i in x_17:     
    x_17 = x_17[1:]     
    print(i, end = " ")
#skrg x_17 udh ga punya a
print('\n')

