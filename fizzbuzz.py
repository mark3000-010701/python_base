a, b = map(int, input().split())
if a > b:
    print("b cần nhập b lớn hơn a")
else:
    for i in range(a, b + 1):
        if (i % 3 == 0 and i % 5 == 0):
            print("fizzbuzz")
        elif i % 5 == 0:
            print("buzz")
        elif i % 3 == 0:
            print("fizz")
        else:
            print(i)
