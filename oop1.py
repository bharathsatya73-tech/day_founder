class employ:
    def fun1(s):
        s.empno = int(input("enter empno :"))
        s.name = input("enter name :")
        s.salary = int(input("enter salary :"))
    def fun2(s):
        print("empno is",s.empno)
        print("name is",s.name)
        print("salary is ", s.salary)
obj = employ()
obj.fun1()
obj.fun2()