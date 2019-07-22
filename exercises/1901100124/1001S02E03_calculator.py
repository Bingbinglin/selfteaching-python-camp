operator=input("选择运算（+、-、*、/）:")
number1=int(input("请输入第一个数字："))
number2=int(input("请输入第二个数字："))
a=number1
b=number2
if operator == "+":
    print(a,"+",b,"=",a+b)
elif operator == "-":
    print(a,"-","=",a-b)
elif operator == "*":
    print(a,"*",b,"=",a*b)
elif operator == "/":
    print(a,"/",b,"=",a/b)
else :
    print("无效运算")
    
    
    
