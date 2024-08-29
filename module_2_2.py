first = int(input())
second = int(input())
third = int(input())

if first == second:
    if first == third:
        print(3)
    else:
        print(2)
elif first == third:
    print(2)
else:
    print(0)