a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

x = a
y = b

while b != 0:
    a, b = b, a % b

gcd = a
lcm = (x * y) // gcd

print("GCD =", gcd)
print("LCM =", lcm)