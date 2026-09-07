class mom:
    def work(s):
        s.clean = int(input("enter cleaning hours :"))
        s.cook = int(input("enter cooking hours :"))
        s.sleep = int(input("enter sleeping hours :"))
    def spend(s):
        print("hours spend in cleaning is :",s.clean)
        print("hours spend in cooking is :",s.cook)
        print("hours spend in sleep is :",s.sleep)
obj = mom()
obj.work()
obj.spend()
    