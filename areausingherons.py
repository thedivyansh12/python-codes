a = float(input("enter the first side of the triangle : "))
b = float(input("enter the second side of the triangle : "))
c = float(input("enter the third side of the triangle : "))
s = (a + b + c) / 2
area  = (s * (s-a) * (s-b) * (s-c)) ** 0.5
print("the area calculated is ", area)
