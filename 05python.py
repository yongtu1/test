'''
if False :
    print('False')
else :
    print('True')

num = int(input('숫자를 입력해 주세요:\n'))

if num % 2 :
    print('홀수입니다.')
else :
    print('짝수입니다.')
    
'''

num = int(input('숫자를 입력해 주세요:\n'))
if num<=30 :
    print('좋음')
elif num<=80 :
    print('보통')
elif num<=150 :
    print('나쁨')
else :
    print('매우나쁨')
    
a=[]
b=[]
for c in range(1,11) :
    if c%2:
        a.append(c)
    else :
        b.append(c)
    c+=1
print(a)
print(b)