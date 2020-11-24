# def per(f,b,a):
#     c=a+b+f
#     print(c)
#     #print("c=",a,"+",b,"+",f,"=",a+b+f)
# per(10,4,6)
g=15
def func(a):
    global g
    g = 10
    print(g)
g=11
func(g)
print(g)