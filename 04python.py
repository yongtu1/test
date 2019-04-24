'''
n=0
while n<5:
    print(f'{n}')
    n+=1
'''

numbers=[1,2,3,4,5,6]
newnumbers=[]

for number in numbers :
    newnumbers.append(number*2)
    print(newnumbers)
    
print(type(newnumbers))

number=[1,2,3,4,5,6,7,8,9]
for a in number:
    for b in number:
        print(f'{a}*{b}={a*b}')