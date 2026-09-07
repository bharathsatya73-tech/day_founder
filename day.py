day = int(input("ENTER DAY :"))
month= int(input("ENTER MONTH :"))
year = int(input("ENTER YEAR :"))

y = year%100
k = y//4
b = 6
if year<2000:
    b= 0
month_codes={
    1: 0,
    2: 3,
    3: 3,
    4: 6,
    5: 1,
    6: 4,
    7: 6,
    8: 2,
    9: 5,
    10: 0,
    11: 3,
    12: 5
}
m = month_codes[month]
l = 0 
if month <=2 and year%4==0 :
    l = -1
result = (y+k+b+l+m+day)%7
days = ["Sunday","Monday","Tuesday","Wednesay","Thursday","Friday","Saturday"]
print("Day:",days[result])
