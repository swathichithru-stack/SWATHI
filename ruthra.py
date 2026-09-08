a=input("Name:")
b=int(input("Age:"))
c=float(input("CGPA:"))
d=float(input("Attendance:"))
e=int(input("Arrears:"))
f=input("Language:")
g=int(input("Coading_score:"))
h=int(input("Comminication_score:"))
skills=["python","java","c++","c"]
eligible = b>=18 and c>=7 and d>=75 and e==0 and f in skills and g>=60 and h>=50
print([" not Eligible", "Eligible"][eligible])

