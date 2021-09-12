print("Welcome User Please enter you name below")
a=input()
b="what is your surname name"
print(b,a)
c=input()
d="enter simple password "
print(d,a,c)
e=input()
print("Username=",a)
print("Password=",e)
print("login here")
Username=input()
if Username == a:
    print("enter password")
else:
    for i in range(1000000):
            print("wrong")
password=input()
if password == e:
    print("text os welcome's ",a,c)
else:
    for i in range(1000000):
            print("wrong")
print("desktop apps")
print("calculator")
print("decimal calculator")
print("notepad")
print("about os")

print("which one do you want")
g=input()
if g == "calculator":
    control="yes"
    while control=="yes":
        print("enter number")
        a,b,c=input().split()
        d=int(a)
        f=int(c)
        if b=="+":
            z=d+f
            print(z)
        elif b=="-":
            z=d-f
            print(z)
        elif b=="*":
            z=d*f
            print(z)
        elif b=="/":
            z=d/f
            print(z)
        else:
            print("incorrect symbol")
        control=input("do you want to continue")
elif g == "decimal calculator":
    control="yes"
    while control=="yes":
        print("enter number")
        a,b,c=input().split()
        d=float(a)
        f=float(c)
        if b=="+":
            z=d+f
            print(z)
        elif b=="-":
            z=d-f
            print(z)
        elif b=="*":
            z=d*f
            print(z)
        elif b=="/":
            z=d/f
            print(z)
        else:
            print("incorrect symbol")
        control=input("do you want to continue")
elif g == "notepad":
    print("Welcome",a,"to notepad")
    h=input()
    print(h,"(Written by ",a,")")
elif g == "about os":
    print("devoloped by VdileepVignesh")
    print("feedback : Vdileepvignesh@gmail.com")
    print("programming language : python")
    print("made on Visual Studio Code")
    print("tested on python IDLE")
    print("python version : 3.9")
    print("Operating system version : text os 1.0")
    print("Operating system : text os")
else:
    for i in range(1000000):
        print("not found")