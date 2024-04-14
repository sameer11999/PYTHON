
l = [3,5,6]
print(l)
print(type(l))
print("\n")

marks = [4,7,8, "Harry", True]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])
print("\n")

print(marks[-3])
print(marks[len(marks)-3])
print(marks[5-3])
print(marks[2])
print("\n")

if 7 in marks:
    print("YES")

else:
    print("NO")
print("\n")

if "Harry" in marks:
    print("YES")

else:
    print("NO")
print("\n")

if "Har" in "Harry":
    print("YES")

else:
    print("NO")
print("\n")

#*********LIST COMPREHENSIONS********

lst = [i for i in range(10)]
print(lst)

lst = [i*i  for i in range(10)]
print(lst)

lst = [i*i  for i in range(10) if(i%2==0)]
print(lst)