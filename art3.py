a = int(input("ENTER THE VALUE :"))
b = int(input("ENTER THE VALUE :"))
c = int(input("ENTER THE VALUE :"))
d = (b*b)-4*a*c
root1 = (-b + (d**(0.5)))/(2*a)
root2 = (-b - (d**(0.5)))/(2*a)
print(f"Roots:{root1,root2}")