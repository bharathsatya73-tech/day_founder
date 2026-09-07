class marks:
    def sinfo(s):
        s.no = int(input("enter sno :"))
        s.name = input("enter name :")
        s.clas = int(input("enter class :"))
    def smarks(s):
        s.maths = int(input("enter maths :"))
        s.physics = int(input("enter physics :"))
        s.chemistry = int(input("enter chemistry :"))
    def results(s):
        s.total = s.maths + s.physics + s.chemistry
        s.average = s.total/3
    def display(s):
        print("total marks :",s.total)
        print("average is :",s.average)   
obj = marks()
obj.sinfo()
obj.smarks()
obj.results()
obj.display()     