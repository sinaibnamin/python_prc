a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

bigger = a if a > b else b
print("Bigger number:", bigger)


if a % 3 == 0 and a % 5 == 0:
    print(a, "is multiple of both 3 and 5")

if b % 3 == 0 and b % 5 == 0:
    print(b, "is multiple of both 3 and 5")

if not ((a % 3 == 0 and a % 5 == 0) or (b % 3 == 0 and b % 5 == 0)):
    print("None of them is multiple of both 3 and 5")
