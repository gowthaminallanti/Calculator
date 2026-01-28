while True:
 a=int(input("enter num1:"))
 b=int(input("enter num2:"))
 operation=input("choose any operation:" )
 if  operation=="+":
        print("sum of a,b is:",a+b)
 elif operation=="-":
        print("sub of a,b is:",a-b)
 elif operation=="*":
        print("mul of a,b is:",a*b)
 elif operation=="/":
    if b==0:
        print("error")
    else:
        print("div of a,b is:",a/b)
 elif operation=="%":
    if b==0:
        print("error")
    else:
        print("mod of a,b is:",a%b)
 again=input("Do you want to try again? (yes/no):")
 if again=="no":
    print("calculator closed")
    break

