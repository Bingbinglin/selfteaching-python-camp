print('九九乘表法')
for i in range(1,10):      #i=1,2,3,4,5,6,7,8,9
    for j in range(1,i+1): #j=[1,2),[1,3),[1,4),[1,5),[1,6),[1,7),[1,8),[1,9),[1,10)
        print(i,'*',j,'=',i*j,end='\t')

 
 
print('奇数九九乘表法')
i=1
while i<10:
    if i%2==0:
        print()
    else:  
        for j in range(1,i+1):
            print(i,'*',j,'=',i*j,end='\t')
    i +=1

print('跳过奇数九九乘法表')   
i=1
while i<10:
    if i%2>0:
    print()
    else:
        for j in range(1,i+1):
            print(i,'*',j,'=',i*j,end='\t')
    i +=1
   
        
print('打不出九九乘法表的原因1')    
for i in range(1,10):   #i=1,2,3,4,5,6,7,8,9
    for j in range(1,10):#j=1,2,3,4,5,6,7,8,9
        print(i,"*",j,"=",i*j,end="\t")
    print()


print('打不出九九乘法表的原因2')   
for i in range(1,10):     #i=1,2,3,4,5,6,7,8,9
    for j in range(i,i+1):#j=1/2/3/4/5/6/7/8/9
        print(i,"*",j,"=",i*j)
    print()


print('改正')
for i in range(1,10):      #i=1,2,3,4,5,6,7,8,9
    for j in range(1,i+1): #j=[1,2),[1,3),[1,4),[1,5),[1,6),[1,7),[1,8),[1,9),[1,10)
        print(i,'*',j,'=',i*j,end='\t')#没有end='\t'，打印出的结果是每行为一个值；作用是将值与值的间隔变为一个tab
    print()#结果与结果之间以换行的方式呈现

    
    








    


