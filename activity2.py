print("Enter a number (numerator)")
numerator = int(input())
print("Enter a number (denominator)")
denominator = int(input())
if numerator % denominator == 0:
    print("\n" +str(numerator) + "is divisible by" +str(denominator))
else:
    print("\n" +str(numerator) + "is not divisible by" +str(denominator))