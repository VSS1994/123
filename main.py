a=float(input("введите число:"))
b=input("выберите действие +-*/:")
c=float(input("введите число:"))
while(b=="+"):
    print(a+c)
    break
while(b=="-"):
    print(a-c)
    break
while(b=="*"):
    print(a*c)
    break
while(b=="/"):
    while(c==0):
        print("fuckoff")
        break
    else:
        while(b=="/"):
            print(a/c)
            break
    break

