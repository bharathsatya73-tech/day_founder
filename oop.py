class student :
    def fun1(s):
        s.sno = int(input("enter sno :"))
        s.name = input("enter  name :")
        s.clas = int(input("enter class :"))
    def fun2(s):
        print("sno is :",s.sno)
        print("name is :",s.name)
        print("class is :",s.clas)
obj = student()
obj.fun1()
obj.fun2()
         