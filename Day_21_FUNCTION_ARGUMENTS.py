
# def average(a,b):
#     print("The average is",(a+b)/2)

# average(4, 6) 

# **********Default Argument*************
# def average(a=8,b=4):
#     print("The average is",(a+b)/2)

# average(b=3) 

def average(*numbers):

    sum = 0

    for i in numbers:
        sum = sum + i
    # print("Average is: ", sum/ len(numbers))
    return sum/ len(numbers)

c = average(5,6,4,8)
print("Average is : ",c)